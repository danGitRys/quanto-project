
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


-- Beispiel: Jeder Mitarbeiter in 10 Projekten mit unterschiedlichen Rollen
INSERT INTO assignment (fk_project, fk_employee, [role])
VALUES
-- Mitarbeiter 2
(1242, 2, 'Member'), (1243, 2, 'Leader'), (1244, 2, 'Admin'), (1245, 2, 'Member'), (1246, 2, 'Leader'),
(1247, 2, 'Admin'), (1248, 2, 'Member'), (1249, 2, 'Leader'), (1250, 2, 'Admin'), (1251, 2, 'Admin'),

-- Mitarbeiter 3
(1243, 3, 'Leader'), (1244, 3, 'Admin'), (1245, 3, 'Member'), (1246, 3, 'Leader'), (1247, 3, 'Admin'),
(1248, 3, 'Member'), (1249, 3, 'Leader'), (1250, 3, 'Admin'), (1251, 3, 'Admin'), (1252, 3, 'Member'),

-- Mitarbeiter 4
(1242, 4, 'Admin'), (1243, 4, 'Member'), (1244, 4, 'Leader'), (1245, 4, 'Admin'), (1246, 4, 'Member'),
(1247, 4, 'Leader'), (1248, 4, 'Admin'), (1249, 4, 'Admin'), (1250, 4, 'Admin'), (1251, 4, 'Leader'),

-- Mitarbeiter 5
(1242, 5, 'Leader'), (1243, 5, 'Admin'), (1244, 5, 'Member'), (1245, 5, 'Leader'), (1246, 5, 'Admin'),
(1247, 5, 'Member'), (1248, 5, 'Leader'), (1249, 5, 'Admin'), (1250, 5, 'Admin'), (1251, 5, 'Member'),

-- Mitarbeiter 6
(1242, 6, 'Admin'), (1243, 6, 'Member'), (1244, 6, 'Leader'), (1245, 6, 'Admin'), (1246, 6, 'Leader'),
(1247, 6, 'Admin'), (1248, 6, 'Member'), (1249, 6, 'Leader'), (1250, 6, 'Admin'), (1251, 6, 'Admin'),

-- Mitarbeiter 7
(1242, 7, 'Leader'), (1243, 7, 'Admin'), (1244, 7, 'Member'), (1245, 7, 'Leader'), (1246, 7, 'Admin'),
(1247, 7, 'Member'), (1248, 7, 'Leader'), (1249, 7, 'Admin'), (1250, 7, 'Admin'), (1251, 7, 'Member'),

-- Mitarbeiter 8
(1242, 8, 'Admin'), (1243, 8, 'Leader'), (1244, 8, 'Member'), (1245, 8, 'Leader'), (1246, 8, 'Admin'),
(1247, 8, 'Member'), (1248, 8, 'Leader'), (1249, 8, 'Admin'), (1250, 8, 'Admin'), (1251, 8, 'Member'),

-- Mitarbeiter 9
(1242, 9, 'Member'), (1243, 9, 'Leader'), (1244, 9, 'Admin'), (1245, 9, 'Leader'), (1246, 9, 'Admin'),
(1247, 9, 'Member'), (1248, 9, 'Leader'), (1249, 9, 'Admin'), (1250, 9, 'Admin'), (1251, 9, 'Member'),

-- Mitarbeiter 10
(1242, 10, 'Admin'), (1243, 10, 'Member'), (1244, 10, 'Leader'), (1245, 10, 'Admin'), (1246, 10, 'Leader'),
(1247, 10, 'Admin'), (1248, 10, 'Member'), (1249, 10, 'Leader'), (1250, 10, 'Admin'), (1251, 10, 'Admin'),

-- Mitarbeiter 11
(1242, 11, 'Leader'), (1243, 11, 'Admin'), (1244, 11, 'Member'), (1245, 11, 'Leader'), (1246, 11, 'Admin'),
(1247, 11, 'Member'), (1248, 11, 'Leader'), (1249, 11, 'Admin'), (1250, 11, 'Admin'), (1251, 11, 'Member'),

-- Mitarbeiter 12
(1242, 12, 'Admin'), (1243, 12, 'Member'), (1244, 12, 'Leader'), (1245, 12, 'Admin'), (1246, 12, 'Leader'),
(1247, 12, 'Admin'), (1248, 12, 'Member'), (1249, 12, 'Leader'), (1250, 12, 'Admin'), (1251, 12, 'Admin'),

-- Mitarbeiter 13
(1242, 13, 'Leader'), (1243, 13, 'Admin'), (1244, 13, 'Member'), (1245, 13, 'Leader'), (1246, 13, 'Admin'),
(1247, 13, 'Member'), (1248, 13, 'Leader'), (1249, 13, 'Admin'), (1250, 13, 'Admin'), (1251, 13, 'Member'),

-- Mitarbeiter 14
(1242, 14, 'Admin'), (1243, 14, 'Member'), (1244, 14, 'Leader'), (1245, 14, 'Admin'), (1246, 14, 'Leader'),
(1247, 14, 'Admin'), (1248, 14, 'Member'), (1249, 14, 'Leader'), (1250, 14, 'Admin'), (1251, 14, 'Admin'),

-- Mitarbeiter 15
(1242, 15, 'Member'), (1243, 15, 'Leader'), (1244, 15, 'Admin'), (1245, 15, 'Member'), (1246, 15, 'Leader'),
(1247, 15, 'Admin'), (1248, 15, 'Member'), (1249, 15, 'Leader'), (1250, 15, 'Admin'), (1251, 15, 'Admin'),

-- Mitarbeiter 16
(1242, 16, 'Admin'), (1243, 16, 'Leader'), (1244, 16, 'Member'), (1245, 16, 'Member'), (1246, 16, 'Member'),
(1247, 16, 'Member'), (1248, 16, 'Member'), (1249, 16, 'Member'), (1250, 16, 'Member'), (1251, 16, 'Member'),

-- Mitarbeiter 1005
(1242, 1005, 'Leader'), (1243, 1005, 'Admin'), (1244, 1005, 'Member'), (1245, 1005, 'Leader'), (1246, 1005, 'Admin'),
(1247, 1005, 'Member'), (1248, 1005, 'Leader'), (1249, 1005, 'Admin'), (1250, 1005, 'Admin'), (1251, 1005, 'Member'),

-- Mitarbeiter 2002
(1242, 2002, 'Admin'), (1243, 2002, 'Leader'), (1244, 2002, 'Member'), (1245, 2002, 'Admin'), (1246, 2002, 'Leader'),
(1247, 2002, 'Member'), (1248, 2002, 'Leader'), (1249, 2002, 'Admin'), (1250, 2002, 'Member'), (1251, 2002, 'Admin'),

-- Mitarbeiter 2003
(1242, 2003, 'Leader'), (1243, 2003, 'Admin'), (1244, 2003, 'Member'), (1245, 2003, 'Leader'), (1246, 2003, 'Admin'),
(1247, 2003, 'Member'), (1248, 2003, 'Leader'), (1249, 2003, 'Admin'), (1250, 2003, 'Admin'), (1251, 2003, 'Member'),

-- Mitarbeiter 2004
(1242, 2004, 'Admin'), (1243, 2004, 'Member'), (1244, 2004, 'Leader'), (1245, 2004, 'Admin'), (1246, 2004, 'Leader'),
(1247, 2004, 'Admin'), (1248, 2004, 'Member'), (1249, 2004, 'Leader'), (1250, 2004, 'Admin'), (1251, 2004, 'Admin'),

-- Mitarbeiter 2005
(1242, 2005, 'Member'), (1243, 2005, 'Leader'), (1244, 2005, 'Admin'), (1245, 2005, 'Member'), (1246, 2005, 'Leader'),
(1247, 2005, 'Admin'), (1248, 2005, 'Member'), (1249, 2005, 'Leader'), (1250, 2005, 'Admin'), (1251, 2005, 'Admin');
