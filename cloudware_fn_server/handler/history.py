import logging

from handler.base_handler import BaseHandler
from dal.history import HistoryRecordDAL


class PostItemHandler(BaseHandler):

    @classmethod
    def process(cls, params):
        # {"user_id": "a6de938aea9101d4fa8a7a3ed3e46999",
        # "secret_text": "Ob8dd6vIU1as1Sra/1MchAMnn/ZI8IUwhjrsRpsOrP0=\n",
        # "device_id": "mRDoxT96WiaJfFh6", "tag_seq": 1632234325673}
        user_id = params.get('user_id')
        secret_text = params.get('secret_text')
        device_id = params.get('device_id')
        tag_seq_id = params.get('tag_seq')
        HistoryRecordDAL.create(seq_id=tag_seq_id, content=secret_text, user_id=user_id, device_id=device_id)
        return {
            'seq_id': tag_seq_id
        }


class GetItemHandler(BaseHandler):

    @classmethod
    def process(cls, params):
        logging.info("params is %s", params)
        # {'user_id': 'a6de938aea9101d4fa8a7a3ed3e46999', 'seq_id': '1632234325673'}
        user_id = params.get('user_id')
        seq_id = params.get('seq_id')
        un_sync_records = HistoryRecordDAL.query_un_sync(user_id=user_id, seq_id=seq_id)
        res = []
        for record in un_sync_records:
            res.append({
                'secret_content': record.content,
                'device_id': record.device_id,
                'seq_id': record.seq_id
            })
        return res


if __name__ == '__main__':
    # PostItemHandler.process({"user_id": "a6de938aea9101d4fa8a7a3ed3e46999", "secret_text": "K2WtSqKsJHshMFODcC3L4AMnn/ZI8IUwhjrsRpsOrP0=\n", "device_id": "mRDoxT96WiaJfFh6", "tag_seq": 1632241526978})
    print(GetItemHandler.process(params={'user_id': 'a6de938aea9101d4fa8a7a3ed3e46999', 'seq_id': '1632241526978'}))
