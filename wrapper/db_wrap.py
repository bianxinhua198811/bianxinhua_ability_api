# @Time     :2019/11/26 11:25
# @Author   :dengyuting
# @File     :db_wrap.py
import pymysql


def setup_hook_clean_db():
    """
    初始化时清理数据库中的历史数据
    :return:
    """
    db = pymysql.connect(host="115.29.205.99",port=3306,user="shiqiurong", password="QGaBlwXT123dfvc7ip",db= "ability_display",charset='utf8')
    cursor = db.cursor()
    try:
        #删除评论
        cursor.execute("delete d from comment d LEFT JOIN  comment a on d.id=a.cid LEFT JOIN question b on a.id = b.id LEFT JOIN departments c on  b.relevantDepartmentId =c.id where   c.company_id =42 and c.enabled = 1")
        cursor.execute("delete d from comment d LEFT JOIN solution a on d.id=a.id LEFT JOIN question b on a.qid = b.id LEFT JOIN departments c on  b.relevantDepartmentId =c.id where   c.company_id =42 and c.enabled = 1")
        cursor.execute("delete d from comment d LEFT JOIN question a on d.id =a.id  LEFT JOIN departments b on  a.relevantDepartmentId =b.id  where b.company_id =42 and b.enabled = 1")
        #删除解决方案
        cursor.execute("delete a from solution a LEFT JOIN question b on a.qid=b.id LEFT JOIN departments c  on b.relevantDepartmentId=c.id where c.company_id =42 and c.enabled = 1")
        #删除问题
        cursor.execute("delete a from question a LEFT JOIN departments b on a.relevantDepartmentId=b.id where b.company_id =42 and b.enabled = 1")
        #删除用户消息表
        cursor.execute("delete a from user_msg a LEFT JOIN user_info b on a.uid=b.uid   where b.company_id=42")
        # 删除用户星数变动表
        cursor.execute("delete a from user_score_change a LEFT JOIN user_info b on a.uid=b.uid   where b.company_id=42")
        # 删除用户解决申请表
        cursor.execute("delete from user_question_solve where uid in (select uid from user_info where company_id=42)")
        # 删除质疑表
        cursor.execute("delete from doubt where company_id=42")
        # 删除额外加分表
        cursor.execute("delete from bonus_point where company_id=42")
        # 删除公告表
        cursor.execute("delete from bulletin where company_id=42")
        # 删除表彰管理表
        cursor.execute("delete from commend where company_id=42")
        # 删除用户消息表
        cursor.execute("delete from user_msg where uid in (select uid from user_info where company_id=42)")
        # 删除用户同感表
        cursor.execute("delete from user_sympathy where uid in (select uid from user_info where company_id=42)")
        # 删除问题标记表
        cursor.execute("delete from question_marks where uid in (select uid from user_info where company_id=42)")
        # 删除问题标记结果表
        cursor.execute("delete from question_marks_result where uid in (select uid from user_info where company_id=42)")
        # 删除用户提交表
        cursor.execute("delete from user_commit where uid in (select uid from user_info where company_id=42)")
        # 删除问题提交表
        cursor.execute("delete a from question_commit a LEFT JOIN user_commit b on a.commitId =b.id LEFT JOIN user_info c on b.uid =c.uid where c.company_id =42")
        db.commit()
        print("delete OK")
    except:
        # 发生错误时回滚
        db.rollback()
    db.close()

def get_solveid(qid):
    #根据问题id，查询相应的解决申请表id
    db = pymysql.connect(host="115.29.205.99", port=3306, user="shiqiurong", password="QGaBlwXT123dfvc7ip",
                         db="ability_display", charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute('select id from user_question_solve where qid = %s',qid)
        result = cursor.fetchone()
        id = result[0]
        return id
    except:
        # 发生错误时回滚
        db.rollback()
    db.close()