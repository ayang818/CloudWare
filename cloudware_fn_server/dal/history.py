from db.base import get_session
from db.history import CWHistoryRecord


class HistoryRecordDAL(object):

    @classmethod
    def create(cls, seq_id, content, user_id, device_id):
        session = get_session()
        record = CWHistoryRecord()
        record.seq_id = seq_id
        record.content = content
        record.user_id = user_id
        record.device_id = device_id
        session.add(record)
        session.commit()

    @classmethod
    def query_un_sync(cls, user_id, seq_id):
        session = get_session()
        record_list = session.query(CWHistoryRecord).filter(CWHistoryRecord.user_id == user_id,
                                                            CWHistoryRecord.seq_id >= seq_id).all()
        return record_list
