create database cloudware_base;

-- 历史纪录表
create table if not exists cw_history_record (
    id bigint unsigned AUTO_INCREMENT comment "主键",
    seq_id bigint unsigned not null comment "seq_id 这条消息的 seq_id",
    content varchar(1000) not null comment "加密内容",
    user_id varchar(200) not null comment "md5(secret_key+salt)",
    device_id varchar(200) not null comment "设备id",
    create_time timestamp not null default CURRENT_TIMESTAMP comment "创建时间",
    update_time  timestamp not null ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP comment "更新时间",
   primary key(id),
   key compact_key(user_id, seq_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;