
/*20 Projekte hinzugefügt*/
INSERT INTO project (p_id, [name], company, [start_date], end_date, fk_creator, creation_date)
VALUES
('P1', 'Frontend', 'FESTO', '2023-12-09', '2023-12-30', 2, GETDATE()),
('P2', 'Backend', 'ABC Corp', '2023-12-10', '2023-12-31', 3, GETDATE()),
('P3', 'Database Design', 'XYZ Ltd', '2023-12-11', '2024-01-01', 4, GETDATE()),
('P4', 'Mobile App', 'Tech Innovations', '2023-12-12', '2024-01-02', 5, GETDATE()),
('P5', 'Data Analytics', 'Data Insights', '2023-12-13', '2024-01-03', 6, GETDATE()),
('P6', 'Security Enhancement', 'SecureTech', '2023-12-14', '2024-01-04', 7, GETDATE()),
('P7', 'AI Integration', 'InnoAI', '2023-12-15', '2024-01-05', 8, GETDATE()),
('P8', 'Cloud Migration', 'CloudTech', '2023-12-16', '2024-01-06', 9, GETDATE()),
('P9', 'E-commerce Platform', 'Shopify', '2023-12-17', '2024-01-07', 10, GETDATE()),
('P10', 'IoT Implementation', 'IoT Innovate', '2023-12-18', '2024-01-08', 11, GETDATE()),
('P11', 'Machine Learning', 'ML Solutions', '2023-12-19', '2024-01-09', 12, GETDATE()),
('P12', 'UI/UX Redesign', 'DesignCo', '2023-12-20', '2024-01-10', 13, GETDATE()),
('P13', 'Network Optimization', 'NetOpt', '2023-12-21', '2024-01-11', 14, GETDATE()),
('P14', 'Blockchain Integration', 'BlockTech', '2023-12-22', '2024-01-12', 15, GETDATE()),
('P15', 'Virtual Reality Project', 'VR Innovate', '2023-12-23', '2024-01-13', 16, GETDATE()),
('P16', 'Social Media Integration', 'SocialTech', '2023-12-24', '2024-01-14', 1005, GETDATE()),
('P17', 'Automation System', 'AutoSys', '2023-12-25', '2024-01-15', 2002, GETDATE()),
('P18', 'Big Data Analytics', 'BigData Co', '2023-12-26', '2024-01-16', 2003, GETDATE()),
('P19', 'Healthcare IT Solutions', 'HealthTech', '2023-12-27', '2024-01-17', 2004, GETDATE()),
('P20', 'Augmented Reality App', 'AR Innovate', '2023-12-28', '2024-01-18', 2005, GETDATE());


/*20 Positionen hinzugefügt*/
INSERT INTO position (position_id, fk_project, rate, wd, volume_total, volume_remaining, [start_date], end_date)
VALUES
('POS1', 1242, 50.0, 40, 100, 80, '2023-12-09', '2023-12-30'),
('POS2', 1243, 45.0, 40, 120, 90, '2023-12-10', '2023-12-31'),
('POS3', 1244, 55.0, 40, 80, 60, '2023-12-11', '2024-01-01'),
('POS4', 1245, 60.0, 40, 150, 120, '2023-12-12', '2024-01-02'),
('POS5', 1246, 70.0, 40, 200, 160, '2023-12-13', '2024-01-03'),
('POS6', 1247, 65.0, 40, 120, 90, '2023-12-14', '2024-01-04'),
('POS7', 1248, 80.0, 40, 180, 140, '2023-12-15', '2024-01-05'),
('POS8', 1249, 75.0, 40, 160, 130, '2023-12-16', '2024-01-06'),
('POS9', 1250, 90.0, 40, 250, 200, '2023-12-17', '2024-01-07'),
('POS10', 1251, 85.0, 40, 300, 240, '2023-12-18', '2024-01-08'),
('POS11', 1252, 100.0, 40, 180, 140, '2023-12-19', '2024-01-09'),
('POS12', 1253, 95.0, 40, 200, 160, '2023-12-20', '2024-01-10'),
('POS13', 1254, 110.0, 40, 220, 180, '2023-12-21', '2024-01-11'),
('POS14', 1255, 105.0, 40, 250, 200, '2023-12-22', '2024-01-12'),
('POS15', 1256, 120.0, 40, 300, 240, '2023-12-23', '2024-01-13'),
('POS16', 1257, 115.0, 40, 120, 90, '2023-12-24', '2024-01-14'),
('POS17', 1258, 130.0, 40, 180, 140, '2023-12-25', '2024-01-15'),
('POS18', 1259, 125.0, 40, 200, 160, '2023-12-26', '2024-01-16'),
('POS19', 1260, 140.0, 40, 220, 180, '2023-12-27', '2024-01-17'),
('POS20', 1261, 135.0, 40, 250, 200, '2023-12-28', '2024-01-18');


