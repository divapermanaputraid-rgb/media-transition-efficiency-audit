CREATE DATABASE "media-transition-efficiency-audit"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


CREATE SCHEMA staging;
CREATE SCHEMA reference;
CREATE SCHEMA mart;

-- 1. Tabel Fact Pengeluaran (Spend)
CREATE TABLE staging.stg_marketing_spend (
	Date DATE,
	CampaignID VARCHAR(50),
	Spend_IDR DECIMAL(18, 2),
	Impressions INT
);

-- 2. Tabel Fact hasil (result)
CREATE TABLE staging.stg_marketing_results (
	Date DATE,
	CampaignID VARCHAR(50),
	Conversions FLOAT,
	Revenue_IDR DECIMAL(18, 2)
);

-- 3. Tabel referensi kampanye
CREATE TABLE reference.ref_campaigns(
	CampaignID VARCHAR(50) PRIMARY KEY,
	Channel VARCHAR(50),
	Sub_Channel VARCHAR(50)
);

-- 4. Tabel referensi kejadian bisnis
CREATE TABLE reference.ref_business_events (
	Date DATE PRIMARY KEY,
	Event_Type VARCHAR (100)
);

-- Tambahkan Foreign Key pada tabel Spend
ALTER TABLE staging.stg_marketing_spend 
ADD CONSTRAINT fk_spend_campaign 
FOREIGN KEY (CampaignID) REFERENCES reference.ref_campaigns(CampaignID);

-- Tambahkan Foreign Key dan kolom audit pada tabel Results
ALTER TABLE staging.stg_marketing_results 
ADD COLUMN is_imputed BOOLEAN DEFAULT FALSE, -- Untuk menandai perbaikan data manual
ADD CONSTRAINT fk_results_campaign 
FOREIGN KEY (CampaignID) REFERENCES reference.ref_campaigns(CampaignID);