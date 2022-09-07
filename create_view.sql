-- SQLite

-- create devices view  
DROP VIEW view_devices;  
CREATE VIEW view_devices AS  
SELECT d.id, t.name as type, d.series_number, d.mfg_date, d.date_of_purchase,d.comment 
FROM devices as d JOIN device_types as t ON d.type = t.id;

-- create records view  
DROP VIEW view_records;  
CREATE VIEW view_records AS  
SELECT dr.id, d.name, d.series_number, p.name as user_name, dr.start_time, dr.end_time, dr.comment, dr.attachment
FROM device_records as dr JOIN devices as d JOIN profiles AS p ON dr.device = d.id and dr.user = p.userId;