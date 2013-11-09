import hashlib
from twisted.enterprise import adbapi
from scrapy import log

# adbapi provides various adapters
# Can easily switch over to other drivers.
# see http://twistedmatrix.com/documents/current/core/howto/rdbms.html
class JobCompanyPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    def _do_upsert(self, conn, item, spider):
        guid = self._get_guid(item)
        conn.execute("""SELECT EXISTS(
                    SELECT 1 FROM company WHERE guid = %s
                )""", (guid, ))
        ret = conn.fetchone()[0]

        guid = self._get_guid(item)

        if ret:
            conn.execute("""
                    UPDATE company SET ad_img = %s, logo = %s, name = %s, tag_line = %s, status = %s, statements = %s,
                           tech_stack = %s, tech_stack_tags = %s, benefits = %s WHERE guid = %s
                """, (item['ad_img'][0], item['logo'][0], item['name'][0], item['tag_line'][0], item['status'][0], '\n'.join(item['statements']),
                      '\n'.join(item['tech_stack']), '\n'.join(item['tech_stack_tags']), '\n'.join(item['benefits']), guid))
        else:
            conn.execute("""
                    INSERT INTO company (guid, ad_img, logo, name, tag_line, status, statements, tech_stack, tech_stack_tags, benefits)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (guid, item['ad_img'][0], item['logo'][0], item['name'][0], item['tag_line'][0], item['status'][0], '\n'.join(item['statements']),
                      '\n'.join(item['tech_stack']), '\n'.join(item['tech_stack_tags']), '\n'.join(item['benefits'])))

    def _handle_error(self, failure, item, spider):
        """Handle occurred on db interaction."""
        # do nothing, just log
        log.err(failure)

    def _get_guid(self, item):
        return hashlib.md5(item['name'][0]).hexdigest()
