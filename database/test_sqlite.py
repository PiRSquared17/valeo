try:
    import sqlite3 as sqlite
except ImportError:
    try:
        import pysqlite2.dbapi2 as sqlite
    except ImportError:
        print "pysqlite can be downloaded at http://initd.org/tracker/pysqlite"
        import sys
        sys.exit()
    
if __name__ == "__main__":
    dbname = "test.db"
    con = sqlite.connect(dbname)
    cur = con.cursor()
    cur.execute("drop table if exists people;")
    cur.execute("create table people (name_last varchar(10), age integer);")
    cur.execute("insert into people (name_last, age) values ('Gutsy',10);")
    cur.execute("insert into people (name_last, age) values ('Ubuntu',7);")
    for name, age in cur.execute("select * from people"):
        print "%s: %d" % (name, age)
