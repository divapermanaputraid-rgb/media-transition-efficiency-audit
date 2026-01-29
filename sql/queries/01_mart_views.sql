-- 1. Membuat Master Table View

CREATE OR REPLACE VIEW mart.vw_master_marketing_performance AS
SELECT
	s.Date,
	c.Channel,
	c.Sub_Channel,
	s.Spend_IDR,

	COALESCE(r.Revenue_IDR, 0) AS Revenue_IDR,
	COALESCE(r.Conversions, 0) AS Conversions,
	-- Audit Flag
	COALESCE(r.is_imputed, FALSE) AS is_imputed,
	-- Integrasi Event
	COALESCE(e.Event_Type, 'Normal Day') AS Event_type,
	-- Kalkulasi ROAS di Database
	CASE
		WHEN s.Spend_IDR > 0 THEN r.Revenue_IDR / s.Spend_IDR
		ELSE 0
	END AS ROAS
FROM staging.stg_marketing_spend s
LEFT JOIN staging.stg_marketing_results r
	ON s.Date = r.Date AND s.CampaignID = r.CampaignID
LEFT JOIN reference.ref_campaigns c
	ON s.CampaignID = c.CampaignID
LEFT JOIN reference.ref_business_events e
	ON s.Date = e.Date;

-- 2. buat performance summary 
CREATE OR REPLACE VIEW mart.vw_annual_performance_summary AS
SELECT
	EXTRACT(YEAR FROM Date) AS Year,
	Channel,
	SUM(Spend_IDR) AS Total_Spend,
	SUM(Revenue_IDR) AS Total_Revenue,
	CASE
		WHEN SUM(Spend_IDR) > 0 THEN SUM(Revenue_IDR) / SUM(Spend_IDR)
		ELSE 0
	END AS Weighted_ROAS
FROM mart.vw_master_marketing_performance
GROUP BY 1, 2;