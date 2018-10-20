import pymysql 

class CapaMedia:

    # It connects to the Auth DB
    def connect_db(self):
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
    def get_user_by_username(self, username):
        connection = self.connect_db()
        try:
            with connection.cursor() as cursor:
                sql_id = "SELECT * FROM `USER_PROFILE` WHERE USERNAME = %s"
                cursor.execute(sql_id, (username,));
                if cursor.rowcount == 0:
                    return make_response('The query did not produce any results (no user found).', HTTPStatus.BAD_REQUEST.value)
                user = cursor.fetchone()
        except pymysql.MySQLError as error:
            print('Got error {!r}, errno is {}'.format(error, error.args[0]))

        connection.close()
        return user

    def getProfile(self, userID, subMenuSelected):
        table_name = "USER_"
        if subMenuSelected == 1:
            table_name = table_name + "PROFILE"
        elif subMenuSelected == 2:
            table_name = table_name + "COUPLE"
        elif subMenuSelected == 3:
            table_name = table_name + "COMPANY"

        connection = self.connect_db()
        try:
            with connection.cursor() as cursor:
                sql_id = "SELECT * FROM `USER_PROFILE` UP INNER JOIN %s OU ON UP.ID_USER = OU.ID_USER WHERE ID_USER = %s"
                cursor.execute(sql_id, (table_name, userID,));
                if cursor.rowcount == 0:
                    return make_response('The query did not produce any results (no user found).', HTTPStatus.BAD_REQUEST.value)
                user = cursor.fetchone()
        except pymysql.MySQLError as error:
            print('Got error {!r}, errno is {}'.format(error, error.args[0]))

        connection.close()
        return user

    def editWork(self, work, userID, subMenuSelected):
        table_name = "USER_"
        if subMenuSelected == 1:
            table_name = table_name + "PROFILE"
        elif subMenuSelected == 2:
            table_name = table_name + "COUPLE"
        elif subMenuSelected == 3:
            table_name = table_name + "COMPANY"

        reg = (username, key[2])
        connection = connect_db()
        cur = connection.cursor()
        sql_id = "update table %s set WORKING = %s WHERE ID_USER = %s"
        cur.execute(sql_id, (table_name, work, userID))
        connection.commit()

    def editStudy(self, study, userID, subMenuSelected):
        table_name = "USER_"
        if subMenuSelected == 1:
            table_name = table_name + "PROFILE"
        elif subMenuSelected == 2:
            table_name = table_name + "COUPLE"
        elif subMenuSelected == 3:
            table_name = table_name + "COMPANY"

        reg = (username, key[2])
        connection = connect_db()
        cur = connection.cursor()
        sql_id = "update table %s set STUDYING = %s WHERE ID_USER = %s"
        cur.execute(sql_id, (table_name, study, userID))
        connection.commit()

    def editGender(self, gender, userID, subMenuSelected):
        table_name = "USER_"
        if subMenuSelected == 1:
            table_name = table_name + "PROFILE"
        elif subMenuSelected == 2:
            table_name = table_name + "COUPLE"
        elif subMenuSelected == 3:
            table_name = table_name + "COMPANY"

        reg = (username, key[2])
        connection = connect_db()
        cur = connection.cursor()
        sql_id = "update table %s set GENDER = %s WHERE ID_USER = %s"
        cur.execute(sql_id, (table_name, gender, userID))
        connection.commit()

    def editDescription(self, description, userID):
        table_name = "USER_"
        if subMenuSelected == 1:
            table_name = table_name + "PROFILE"
        elif subMenuSelected == 2:
            table_name = table_name + "COUPLE"
        elif subMenuSelected == 3:
            table_name = table_name + "COMPANY"

        reg = (username, key[2])
        connection = connect_db()
        cur = connection.cursor()
        sql_id = "update table %s set DESCRIPTION = %s WHERE ID_USER = %s"
        cur.execute(sql_id, (table_name, description, userID))
        connection.commit()

    def editAge(self, age, userID):
        table_name = "USER_PROFILE"
        reg = (username, key[2])
        connection = connect_db()
        cur = connection.cursor()
        sql_id = "update table %s set AGE = %s WHERE ID_USER = %s"
        cur.execute(sql_id, (table_name, age, userID))
        connection.commit()

    def getAllInterestsTable(self):
        return ""

    def addTags(self,userID, nuevosIntereses2):
        reg = (username, key[2])
        connection = connect_db()
        cur = connection.cursor()
        sql_id = "INSERT INTO `USER_PROFILE` (`USERNAME`, `BASE`)  VALUES(%s, %s)"
        cur.execute(sql_id, reg)
        connection.commit()

        insert into "INTEREST_ TABLA SEGUN QUE TE PIDAN" VALUES("ID_USER","ID_TAG")

    def getMatches(self, userID):
        return ""
