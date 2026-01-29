-- 1. ANALISIS EFISIENSI KANAL (Ranking menggunakan Window Function)
--- Mencari kanal mana yang paling efisien di tiap tahun

WITH channel_stats AS (
	SELECT
		Year,
		Channel,
		Weighted_ROAS,
		RANK() OVER(PARTITION BY Year ORDER BY Weighted_ROAS DESC) as efficiency_rank
	FROM mart.vw_annual_performance_summary
)
SELECT * FROM channel_stats WHERE efficiency_rank = 1;

-- 2. DETEKSI ANOMALI 
-- mencari hari kita bakar uang > Rp 50jt tapi revenue = 0
SELECT
	Date,
	Channel,
	Spend_IDR,
	Revenue_IDR,
	Event_Type
FROM mart.vw_master_marketing_performance
WHERE Spend_IDR > 50000000 AND Revenue_IDR = 0
ORDER BY Spend_IDR DESC;

-- 3. analisis Pertumbuhan bulanan
-- lihat tren peforma digital secara kronologis
WITH monthly_data AS (
	SELECT
		DATE_TRUNC('month', Date) as month,
		SUM(Spend_IDR) as total_spend,
		SUM(Revenue_IDR) as total_revenue
	FROM mart.vw_master_marketing_performance
	WHERE Channel = 'Digital'
	GROUP BY 1
)

SELECT
	month,
	total_spend,
	total_revenue,
	LAG(total_revenue) OVER(ORDER BY month) as prev_month_revenue,
	(total_revenue - LAG(total_revenue)OVER(ORDER BY month)) / NULLIF(LAG(total_revenue) OVER(ORDER BY month), 0) * 100 as growth_pct
FROM monthly_data;