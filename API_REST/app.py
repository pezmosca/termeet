from flask import Flask, request
import requests


import logging
import re
import os
import gettext
from io import StringIO
from binascii import hexlify
from functools import partial, wraps

import paramiko

import sqlite3

import pymysql

from flask import send_from_directory

app = Flask(__name__)

url = "https://slack.com/api"


def ssh_key_string_to_obj(text, password=None):
    key = None
    try:
        key = paramiko.RSAKey.from_private_key(StringIO(text), password=password)
    except paramiko.SSHException:
        pass

    try:
        key = paramiko.DSSKey.from_private_key(StringIO(text), password=password)
    except paramiko.SSHException:
        pass
    return key

def ssh_pubkey_gen(private_key=None, username='jumpserver', hostname='localhost'):
    if isinstance(private_key, str):
        private_key = ssh_key_string_to_obj(private_key)

    if not isinstance(private_key, (paramiko.RSAKey, paramiko.DSSKey)):
        raise IOError('Invalid private key')

    public_key = "%(key_type)s %(key_content)s %(username)s@%(hostname)s" % {
        'key_type': private_key.get_name(),
        'key_content': private_key.get_base64(),
        'username': username,
        'hostname': hostname,
    }
    return public_key

def ssh_key_gen(length=1024, type='rsa', password=None, username='jumpserver', hostname=None):
    """Generate user ssh private and public key

    Use paramiko RSAKey generate it.
    :return private key str and public key str
    """

    if hostname is None:
        hostname = os.uname()[1]

    f = StringIO()

    try:
        if type == 'rsa':
            private_key_obj = paramiko.RSAKey.generate(length)
        elif type == 'dsa':
            private_key_obj = paramiko.DSSKey.generate(length)
        else:
            raise IOError('SSH private key must be `rsa` or `dsa`')
        private_key_obj.write_private_key(f, password=password)
        private_key = f.getvalue()
        base64 = private_key_obj.get_base64()
        public_key = ssh_pubkey_gen(private_key_obj, username=username, hostname=hostname)
        return private_key, public_key, base64
    except IOError:
        raise IOError('These is error when generate ssh key.')


# It connects to the Auth DB
def connect_db():
    #create table sessions (user_id bigint(20) unsigned not null, public_uuid varchar(50) not null, token varchar(500), primary key(user_id));
    connection = pymysql.connect(host = os.environ.get("AUTH_DB_HOST"),
                           user = os.environ.get("AUTH_DB_USERNAME"),
                           passwd = os.environ.get("AUTH_DB_PASSWORD"),
                           db = os.environ.get("AUTH_DB_NAME"),
                           port = 3306,
                           cursorclass = pymysql.cursors.DictCursor,
                           connect_timeout = 5)
    return connection


# Giving a WP username it returns the whole WP info of the user
def get_user_by_id(userID, subMenuSelected):
    user = "BAD"
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql_id = "SELECT * FROM `USER_PROFILE` UP INNER JOIN %s OU ON UP.ID_USER = OU.ID_USER WHERE ID_USER = %s"
            cursor.execute(sql_id, (subMenuSelected, userID,));
            if cursor.rowcount == 0:
                return make_response('The query did not produce any results (no user found).', HTTPStatus.BAD_REQUEST.value)
            user = cursor.fetchone()
    except pymysql.MySQLError as error:
        print('Got error {!r}, errno is {}'.format(error, error.args[0]))

    connection.close()
    return user

def getProfile(userID, subMenuSelected):
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql_id = "SELECT * FROM `USER_PROFILE` UP INNER JOIN %s OU ON UP.ID_USER = OU.ID_USER WHERE ID_USER = %s"
            cursor.execute(sql_id, (subMenuSelected, userID,));
            if cursor.rowcount == 0:
                return make_response('The query did not produce any results (no user found).', HTTPStatus.BAD_REQUEST.value)
            user = cursor.fetchone()
    except pymysql.MySQLError as error:
        print('Got error {!r}, errno is {}'.format(error, error.args[0]))

    connection.close()
    return user


@app.route("/")
def hello():
    ####TOKEN
    code = request.args.get("code")
    payload = "code=" + code + "&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2F"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic NDE2ODY5NzU4MTY3LjQ2MDcyMjk5NzkyNTo1MjQ4Y2Q4OGJmMTczNjdhZjJkMWJlM2FkMjI0MTUwYg=="
        }
    response = requests.request("POST", url + "/oauth.access", data=payload, headers=headers)

    user_id = response.json()["user"]["id"]

    token = str(response.json()["access_token"])
    token = "Bearer " + token

    payload = ""
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': token
    }

    response = requests.request("GET", url + "/users.profile.get", data=payload, headers=headers)

    username = response.json()["profile"]["display_name"]

    key = ssh_key_gen(username=username)



    print key[0]
    print key[1]
    print key[2]

    fd = open("private_key.pem", "wb")
    fd.write(key[0])
    fd.close()



    reg = (username, key[2])
    connection = connect_db()
    cur = connection.cursor()
    sql_id = "INSERT INTO `USER_PROFILE` (`USERNAME`, `BASE`)  VALUES(%s, %s)"
    cur.execute(sql_id, reg)
    connection.commit()

    #con_bd = sqlite3.connect('../users.db')
    #cursor_agenda = con_bd.cursor()
    #cursor_agenda.execute("INSERT INTO logins VALUES(?,?,?)", reg)
    #cursor_agenda.close()
    #con_bd.commit()
    #con_bd.close()


    #print response.json()["profile"]["real_name"]

    #return str(response.json())
    #return payload

    return send_from_directory(".", "private_key.pem")

@app.route("/hello")
def hello2():
    user = get_user_by_id(1,1)
    return user['ID_SLACK']

@app.route("/prueba")
def hey():
    user = getProfile(1,1)
    return user
