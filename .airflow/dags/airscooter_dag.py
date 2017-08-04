
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2017, 8, 4),
    'schedule_interval': '@once',
}

dag = DAG('airscooter_dag', default_args=default_args, schedule_interval=timedelta(1))
    

var_open_market_order_omo_charges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-market-order-omo-charges/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_performance_directory_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-performance-directory-2016/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_directory_2013_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-directory-2013-2014/depositor.py", task_id="depositor", dag=dag)

var_vehicle_classification_counts_2012_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/vehicle-classification-counts-2012-2013/depositor.py", task_id="depositor", dag=dag)

var_capital_grants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capital-grants/depositor.py", task_id="depositor", dag=dag)

var_nyc_doe_2015_2016_final_class_size_report_middle_high_school_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-doe-2015-2016-final-class-size-report-middle-high-school/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_directory_2014_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-directory-2014-2015/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_supervision_passthrough_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-supervision-passthrough-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_weekend_traffic_updates_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weekend-traffic-updates/depositor.py", task_id="depositor", dag=dag)

var_weekend_traffic_updates_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weekend-traffic-updates/transform.py", task_id="transform", dag=dag)

var_minority_and_women_owned_business_enterprise_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/minority-and-women-owned-business-enterprise-statistics/depositor.py", task_id="depositor", dag=dag)

var_nyc_wi_fi_hotspot_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-wi-fi-hotspot-locations/depositor.py", task_id="depositor", dag=dag)

var_nycgov_web_analytics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycgov-web-analytics/depositor.py", task_id="depositor", dag=dag)

var_fiscal_2013_appendices_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fiscal-2013-appendices/depositor.py", task_id="depositor", dag=dag)

var_fiscal_2013_appendices_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fiscal-2013-appendices/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_school_level_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-school-level-all-students/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_offensive_language_allegations_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-offensive-language-allegations-2007/depositor.py", task_id="depositor", dag=dag)

var_historical_data_of_foreign_born_population_in_new_york_city_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/historical-data-of-foreign-born-population-in-new-york-city/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_citywide_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-citywide-all-students/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_boro_by_disability_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-boro-by-disability-status/depositor.py", task_id="depositor", dag=dag)

var_prompt_payment_interest_rates_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/prompt-payment-interest-rates/depositor.py", task_id="depositor", dag=dag)

var_where_incidents_that_led_to_a_complaint_took_place_by_precinct_brooklyn_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-complaint-took-place-by-precinct-brooklyn-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_street_name_dictionary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-name-dictionary/depositor.py", task_id="depositor", dag=dag)

var_street_name_dictionary_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-name-dictionary/transform.py", task_id="transform", dag=dag)

var_dof_condominium_comparable_rental_income_manhattan_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-manhattan-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_recreational_boating_permits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/recreational-boating-permits/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_queens_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-queens-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_bid_tabulations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bid-tabulations/depositor.py", task_id="depositor", dag=dag)

var_2014_2015_school_quality_reports_results_for_elementary_middle_and_k_8_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-2015-school-quality-reports-results-for-elementary-middle-and-k-8-schools/depositor.py", task_id="depositor", dag=dag)

var_2014_2015_school_quality_reports_results_for_elementary_middle_and_k_8_schools_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-2015-school-quality-reports-results-for-elementary-middle-and-k-8-schools/transform.py", task_id="transform", dag=dag)

var_expense_all_funds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-all-funds/depositor.py", task_id="depositor", dag=dag)

var_ccr_annual_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccr-annual-report/depositor.py", task_id="depositor", dag=dag)

var_police_department_disciplinary_penalties_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/police-department-disciplinary-penalties/depositor.py", task_id="depositor", dag=dag)

var_open_balance_bronx_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-balance-bronx/depositor.py", task_id="depositor", dag=dag)

var_open_balance_bronx_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-balance-bronx/transform.py", task_id="transform", dag=dag)

var_demographics_and_profiles_at_the_public_use_microdata_area_puma_subarea_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographics-and-profiles-at-the-public-use-microdata-area-puma-subarea-level/depositor.py", task_id="depositor", dag=dag)

var_demographics_and_profiles_at_the_public_use_microdata_area_puma_subarea_level_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographics-and-profiles-at-the-public-use-microdata-area-puma-subarea-level/transform.py", task_id="transform", dag=dag)

var_dycd_after_school_programs_reading_and_writing_literacy_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-reading-and-writing-literacy-programs/depositor.py", task_id="depositor", dag=dag)

var_transportable_classroom_units_buildings_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/transportable-classroom-units-buildings-schools/depositor.py", task_id="depositor", dag=dag)

var_current_rfp_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/current-rfp/depositor.py", task_id="depositor", dag=dag)

var_nypd_sectors_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nypd-sectors/depositor.py", task_id="depositor", dag=dag)

var_broadway_events_calendar_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/broadway-events-calendar/depositor.py", task_id="depositor", dag=dag)

var_broadway_events_calendar_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/broadway-events-calendar/transform.py", task_id="transform", dag=dag)

var_workforce1_job_listing_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/workforce1-job-listing/depositor.py", task_id="depositor", dag=dag)

var_municipal_court_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-court-districts/depositor.py", task_id="depositor", dag=dag)

var_2010_census_blocks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-census-blocks/depositor.py", task_id="depositor", dag=dag)

var_dycd_rhy_runaway_and_homeless_youth_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-rhy-runaway-and-homeless-youth-services/depositor.py", task_id="depositor", dag=dag)

var_lion_differences_file_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lion-differences-file/depositor.py", task_id="depositor", dag=dag)

var_lion_differences_file_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lion-differences-file/transform.py", task_id="transform", dag=dag)

var_sea_level_rise_maps_2020s_100_year_floodplain_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sea-level-rise-maps-2020s-100-year-floodplain/depositor.py", task_id="depositor", dag=dag)

var_directory_of_bronx_future_parks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-bronx-future-parks/depositor.py", task_id="depositor", dag=dag)

var_votingpoll_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/votingpoll-sites/depositor.py", task_id="depositor", dag=dag)

var_school_monitoring_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-monitoring-data/depositor.py", task_id="depositor", dag=dag)

var_fy15_mmr_data_extract_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy15-mmr-data-extract/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_of_2005_2011_total_cohort_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-of-2005-2011-total-cohort/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_population_by_borough_1950_2040_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-population-by-borough-1950-2040/depositor.py", task_id="depositor", dag=dag)

var_oace_office_of_adult_and_continuing_education_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/oace-office-of-adult-and-continuing-education-sites/depositor.py", task_id="depositor", dag=dag)

var_daily_inmates_in_custody_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/daily-inmates-in-custody/depositor.py", task_id="depositor", dag=dag)

var_schoolyards_to_playgrounds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/schoolyards-to-playgrounds/depositor.py", task_id="depositor", dag=dag)

var_inspections_requested_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inspections-requested/depositor.py", task_id="depositor", dag=dag)

var_water_use_restrictions_summary_of_15_rcny_chapters_20_and_21_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/water-use-restrictions-summary-of-15-rcny-chapters-20-and-21/depositor.py", task_id="depositor", dag=dag)

var_fy16_mmr_agency_performance_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy16-mmr-agency-performance-indicators/depositor.py", task_id="depositor", dag=dag)

var_2010_census_blocks_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-census-blocks-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_nyc_thru_truck_routes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-thru-truck-routes/depositor.py", task_id="depositor", dag=dag)

var_nyc_thru_truck_routes_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-thru-truck-routes/transform.py", task_id="transform", dag=dag)

var_directory_of_zoning_details_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-zoning-details/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nyc_cable_providers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nyc-cable-providers/depositor.py", task_id="depositor", dag=dag)

var_commuter_van_services_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/commuter-van-services-drivers/depositor.py", task_id="depositor", dag=dag)

var_commuter_van_services_drivers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/commuter-van-services-drivers/transform.py", task_id="transform", dag=dag)

var_math_test_results_2006_2012_borough_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-borough-ell/depositor.py", task_id="depositor", dag=dag)

var_contractor_sub_contractor_change_order_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/contractor-sub-contractor-change-order-report/depositor.py", task_id="depositor", dag=dag)

var_historical_driver_application_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/historical-driver-application-status/depositor.py", task_id="depositor", dag=dag)

var_median_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/median/depositor.py", task_id="depositor", dag=dag)

var_izone_pls_school_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/izone-pls-school-list/depositor.py", task_id="depositor", dag=dag)

var_home_care_caseload_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/home-care-caseload/depositor.py", task_id="depositor", dag=dag)

var_catch_basin_inspection_and_cleaning_activity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/catch-basin-inspection-and-cleaning-activity/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_citywide_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-citywide-swd/depositor.py", task_id="depositor", dag=dag)

var_housing_maintenance_code_violations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/housing-maintenance-code-violations/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_health_and_hospitals_corporation_hhc_hhc_options_family_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-health-and-hospitals-corporation-hhc-hhc-options-family-level/depositor.py", task_id="depositor", dag=dag)

var_gender_of_subject_officers_compared_to_new_york_city_police_department_demographics_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/gender-of-subject-officers-compared-to-new-york-city-police-department-demographics-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_damage_by_sandy_by_age_of_building_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/damage-by-sandy-by-age-of-building/depositor.py", task_id="depositor", dag=dag)

var_fy17_pmmr_agency_performance_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy17-pmmr-agency-performance-indicators/depositor.py", task_id="depositor", dag=dag)

var_city_store_the_official_store_of_the_city_of_new_york_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-store-the-official-store-of-the-city-of-new-york/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_staten_island_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-staten-island-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_citywide_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-gender/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_tax_revenue_fy_1980_fy_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-tax-revenue-fy-1980-fy-2014/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_osy_out_of_school_youth_employment_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-osy-out-of-school-youth-employment-programs/depositor.py", task_id="depositor", dag=dag)

var_nycha_application_priority_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-application-priority-codes/depositor.py", task_id="depositor", dag=dag)

var_2000_census_blocks_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2000-census-blocks-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_subway_stations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/subway-stations/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_borough_classes_of_2005_2011_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-borough-classes-of-2005-2011-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_residential_water_use_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/residential-water-use/depositor.py", task_id="depositor", dag=dag)

var_doing_business_search_people_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doing-business-search-people/depositor.py", task_id="depositor", dag=dag)

var_borough_enrollment_centers_additional_ways_to_graduate_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/borough-enrollment-centers-additional-ways-to-graduate/depositor.py", task_id="depositor", dag=dag)

var_housing_maintenance_code_complaints_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/housing-maintenance-code-complaints/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_citywide_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-citywide-ell/depositor.py", task_id="depositor", dag=dag)

var_2010_local_film_festivals_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-local-film-festivals/depositor.py", task_id="depositor", dag=dag)

var_legally_operating_businesses_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/legally-operating-businesses/depositor.py", task_id="depositor", dag=dag)

var_cash_assistance_heads_of_household_by_engagement_16_24_years_old_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cash-assistance-heads-of-household-by-engagement-16-24-years-old/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_offensive_language_allegations_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-offensive-language-allegations-2008/depositor.py", task_id="depositor", dag=dag)

var_dcas_managed_public_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcas-managed-public-buildings/depositor.py", task_id="depositor", dag=dag)

var_inmate_discharges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-discharges/depositor.py", task_id="depositor", dag=dag)

var_2006_07_class_size_school_level_detail_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2006-07-class-size-school-level-detail/depositor.py", task_id="depositor", dag=dag)

var_incident_based_distribution_of_readyny_guides_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/incident-based-distribution-of-readyny-guides/depositor.py", task_id="depositor", dag=dag)

var_directory_of_competitive_bid_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-competitive-bid/depositor.py", task_id="depositor", dag=dag)

var_strategic_plan_progress_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/strategic-plan-progress-report/depositor.py", task_id="depositor", dag=dag)

var_medicaid_buy_in_program_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medicaid-buy-in-program-income-levels/depositor.py", task_id="depositor", dag=dag)

var_citywide_cash_assistance_cases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citywide-cash-assistance-cases/depositor.py", task_id="depositor", dag=dag)

var_dob_violations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-violations/depositor.py", task_id="depositor", dag=dag)

var_universal_pre_k_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/universal-pre-k/depositor.py", task_id="depositor", dag=dag)

var_street_hail_livery_shl_permits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-hail-livery-shl-permits/depositor.py", task_id="depositor", dag=dag)

var_dcla_program_funding_for_fy11_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-program-funding-for-fy11/depositor.py", task_id="depositor", dag=dag)

var_city_record_online_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-record-online/depositor.py", task_id="depositor", dag=dag)

var_directory_of_counseling_advocacy_and_other_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-counseling-advocacy-and-other-services/depositor.py", task_id="depositor", dag=dag)

var_jamica_center_bid_businesses_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/jamica-center-bid-businesses/depositor.py", task_id="depositor", dag=dag)

var_2009_school_survey_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2009-school-survey/depositor.py", task_id="depositor", dag=dag)

var_2009_school_survey_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2009-school-survey/transform.py", task_id="transform", dag=dag)

var_inmate_incidents_inmate_fights_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-incidents-inmate-fights/depositor.py", task_id="depositor", dag=dag)

var_stealth_fiber_map_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/stealth-fiber-map/depositor.py", task_id="depositor", dag=dag)

var_assembly_district_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/assembly-district-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_manhattan_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-manhattan-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_jobs_and_internships_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-jobs-and-internships/depositor.py", task_id="depositor", dag=dag)

var_foil_report_all_markets_approved_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/foil-report-all-markets-approved/depositor.py", task_id="depositor", dag=dag)

var_shoreline_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/shoreline/depositor.py", task_id="depositor", dag=dag)

var_upcoming_contracts_to_be_awarded_cip_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/upcoming-contracts-to-be-awarded-cip/depositor.py", task_id="depositor", dag=dag)

var_nyc_parks_daily_tasks_cleaning_records_fiscal_year_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-parks-daily-tasks-cleaning-records-fiscal-year-2016/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_transit_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-transit-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_projected_public_school_ratio_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-public-school-ratio/depositor.py", task_id="depositor", dag=dag)

var_2011_2012_nyc_family_guides_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2011-2012-nyc-family-guides/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_borough_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-borough-swd/depositor.py", task_id="depositor", dag=dag)

var_energy_and_water_data_disclosure_for_local_law_84_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-and-water-data-disclosure-for-local-law-84-2012/depositor.py", task_id="depositor", dag=dag)

var_school_progress_reports_all_schools_2010_11_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-reports-all-schools-2010-11/depositor.py", task_id="depositor", dag=dag)

var_total_allegations_and_total_complaints_received_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/total-allegations-and-total-complaints-received-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_staten_island_ferry_schedule_gtfs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/staten-island-ferry-schedule-gtfs/depositor.py", task_id="depositor", dag=dag)

var_staten_island_ferry_schedule_gtfs_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/staten-island-ferry-schedule-gtfs/transform.py", task_id="transform", dag=dag)

var_times_square_entertainment_venues_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-entertainment-venues/depositor.py", task_id="depositor", dag=dag)

var_forestry_service_requests_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/forestry-service-requests/depositor.py", task_id="depositor", dag=dag)

var_day_care_center_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/day-care-center/depositor.py", task_id="depositor", dag=dag)

var_2017_2018_school_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2017-2018-school-zones/depositor.py", task_id="depositor", dag=dag)

var_luxury_limousine_services_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/luxury-limousine-services-vehicles/depositor.py", task_id="depositor", dag=dag)

var_luxury_limousine_services_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/luxury-limousine-services-vehicles/transform.py", task_id="transform", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_boro_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-boro-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_directory_of_unsheltered_street_homeless_to_general_population_ratio_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-unsheltered-street-homeless-to-general-population-ratio-2012/depositor.py", task_id="depositor", dag=dag)

var_clear_channel_sign_list_times_sqaure_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/clear-channel-sign-list-times-sqaure/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_nda_educational_middle_school_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-nda-educational-middle-school-programs/depositor.py", task_id="depositor", dag=dag)

var_sea_level_rise_maps_2020s_500_year_floodplain_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sea-level-rise-maps-2020s-500-year-floodplain/depositor.py", task_id="depositor", dag=dag)

var_new_york_state_english_language_arts_ela_exam_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-state-english-language-arts-ela-exam/depositor.py", task_id="depositor", dag=dag)

var_competitiveness_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/competitiveness/depositor.py", task_id="depositor", dag=dag)

var_competitiveness_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/competitiveness/transform.py", task_id="transform", dag=dag)

var_pmmr_raw_data_fy_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/pmmr-raw-data-fy-2013/depositor.py", task_id="depositor", dag=dag)

var_transportation_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/transportation-sites/depositor.py", task_id="depositor", dag=dag)

var_historic_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/historic-districts/depositor.py", task_id="depositor", dag=dag)

var_where_civilian_complaints_were_reported_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-civilian-complaints-were-reported-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_wi_fi_hotspot_locations_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-wi-fi-hotspot-locations-2/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_school_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-school-ell/depositor.py", task_id="depositor", dag=dag)

var_dep_bureau_of_wastewater_treatment_bwt_2010_nuisance_complaints_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-bureau-of-wastewater-treatment-bwt-2010-nuisance-complaints/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_special_operations_division_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-special-operations-division-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_civil_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/civil-list/depositor.py", task_id="depositor", dag=dag)

var_dsny_monthly_tonnage_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dsny-monthly-tonnage-data/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_case_closings_by_reason_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-case-closings-by-reason/depositor.py", task_id="depositor", dag=dag)

var_fair_student_funding_budget_detail_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fair-student-funding-budget-detail-2/depositor.py", task_id="depositor", dag=dag)

var_weekday_traffic_updates_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weekday-traffic-updates/depositor.py", task_id="depositor", dag=dag)

var_weekday_traffic_updates_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weekday-traffic-updates/transform.py", task_id="transform", dag=dag)

var_recurring_resident_economic_empowerment_and_sustainability_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/recurring-resident-economic-empowerment-and-sustainability-programs/depositor.py", task_id="depositor", dag=dag)

var_new_jersey_transit_station_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-jersey-transit-station/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_school_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-school-all-students/depositor.py", task_id="depositor", dag=dag)

var_registration_contacts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/registration-contacts/depositor.py", task_id="depositor", dag=dag)

var_zoning_gis_data_geodatabase_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zoning-gis-data-geodatabase/depositor.py", task_id="depositor", dag=dag)

var_zoning_gis_data_geodatabase_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zoning-gis-data-geodatabase/transform.py", task_id="transform", dag=dag)

var_dob_now_safety_facades_compliance_filings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-now-safety-facades-compliance-filings/depositor.py", task_id="depositor", dag=dag)

var_tenure_of_officers_against_whom_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tenure-of-officers-against-whom-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_abuse_of_authority_allegations_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-abuse-of-authority-allegations-2009/depositor.py", task_id="depositor", dag=dag)

var_2040_population_projection_tables_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2040-population-projection-tables/depositor.py", task_id="depositor", dag=dag)

var_2040_population_projection_tables_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2040-population-projection-tables/transform.py", task_id="transform", dag=dag)

var_dop_juvenile_cases_snapshot_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-cases-snapshot-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_distribution_of_offensive_language_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/distribution-of-offensive-language-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_immigrant_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-immigrant-services/depositor.py", task_id="depositor", dag=dag)

var_cash_assistance_engagement_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cash-assistance-engagement-report/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2009_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2009/transform.py", task_id="transform", dag=dag)

var_where_incidents_that_led_to_a_complaint_took_place_by_precinct_bronx_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-complaint-took-place-by-precinct-bronx-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dep_cryptosporidium_and_giardia_data_set_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-cryptosporidium-and-giardia-data-set/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_in_queens_for_class_1_2_and_3_family_homes_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2008/depositor.py", task_id="depositor", dag=dag)

var_nyc_local_truck_routes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-local-truck-routes/depositor.py", task_id="depositor", dag=dag)

var_nyc_local_truck_routes_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-local-truck-routes/transform.py", task_id="transform", dag=dag)

var_nyc_city_hall_library_catalog_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-city-hall-library-catalog/depositor.py", task_id="depositor", dag=dag)

var_distribution_of_abuse_of_authority_allegations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/distribution-of-abuse-of-authority-allegations/depositor.py", task_id="depositor", dag=dag)

var_completed_percent_for_art_projects_with_artist_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/completed-percent-for-art-projects-with-artist-information/depositor.py", task_id="depositor", dag=dag)

var_medallion_vehicles_authorized_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medallion-vehicles-authorized/depositor.py", task_id="depositor", dag=dag)

var_hispanic_population_by_selected_subgroups_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hispanic-population-by-selected-subgroups-by-borough/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_nda_educational_high_school_progams_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-nda-educational-high-school-progams/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_district_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-district-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_directory_of_running_tracks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-running-tracks/depositor.py", task_id="depositor", dag=dag)

var_directory_of_running_tracks_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-running-tracks/transform.py", task_id="transform", dag=dag)

var_zoning_gis_data_shapefile_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zoning-gis-data-shapefile/depositor.py", task_id="depositor", dag=dag)

var_railroad_line_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/railroad-line/depositor.py", task_id="depositor", dag=dag)

var_2016_nyc_open_data_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2016-nyc-open-data-plan/depositor.py", task_id="depositor", dag=dag)

var_paratransit_services_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-services-drivers/depositor.py", task_id="depositor", dag=dag)

var_paratransit_services_drivers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-services-drivers/transform.py", task_id="transform", dag=dag)

var_linknyc_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/linknyc-locations/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_offensive_language_allegations_2006_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-offensive-language-allegations-2006/depositor.py", task_id="depositor", dag=dag)

var_application_for_state_aid_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/application-for-state-aid/depositor.py", task_id="depositor", dag=dag)

var_total_hasa_cases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/total-hasa-cases/depositor.py", task_id="depositor", dag=dag)

var_path_station_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/path-station-locations/depositor.py", task_id="depositor", dag=dag)

var_municipal_court_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-court-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_force_allegations_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-force-allegations-2009/depositor.py", task_id="depositor", dag=dag)

var_environmentally_preferable_purchasing_fy15_goods_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/environmentally-preferable-purchasing-fy15-goods/depositor.py", task_id="depositor", dag=dag)

var_benefits_and_programs_api_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/benefits-and-programs-api/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_nda_youth_employment_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-nda-youth-employment-programs/depositor.py", task_id="depositor", dag=dag)

var_nyc_taxi_and_limousine_commission_authorized_dispatch_service_providers_dsp_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-taxi-and-limousine-commission-authorized-dispatch-service-providers-dsp/depositor.py", task_id="depositor", dag=dag)

var_bi_annual_pedestrian_counts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bi-annual-pedestrian-counts/depositor.py", task_id="depositor", dag=dag)

var_production_office_space_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/production-office-space/depositor.py", task_id="depositor", dag=dag)

var_doing_business_search_entities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doing-business-search-entities/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_teen_action_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-teen-action-programs/depositor.py", task_id="depositor", dag=dag)

var_beaches_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/beaches/depositor.py", task_id="depositor", dag=dag)

var_historical_dob_permit_issuance_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/historical-dob-permit-issuance/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_manhattan_north_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-manhattan-north-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_rudy_w_giuliani_1994_2001_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/rudy-w-giuliani-1994-2001/depositor.py", task_id="depositor", dag=dag)

var_rudy_w_giuliani_1994_2001_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/rudy-w-giuliani-1994-2001/transform.py", task_id="transform", dag=dag)

var_golf_courses_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/golf-courses/depositor.py", task_id="depositor", dag=dag)

var_map_of_nycha_developments_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/map-of-nycha-developments/depositor.py", task_id="depositor", dag=dag)

var_basin_town_county_2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/basin-town-county-2010/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_drivers_who_have_completed_passenger_assistance_training_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-drivers-who-have-completed-passenger-assistance-training/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_drivers_who_have_completed_passenger_assistance_training_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-drivers-who-have-completed-passenger-assistance-training/transform.py", task_id="transform", dag=dag)

var_hpd_project_building_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-project-building-element/depositor.py", task_id="depositor", dag=dag)

var_inclusionary_housing_designated_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inclusionary-housing-designated-areas/depositor.py", task_id="depositor", dag=dag)

var_mapped_in_ny_companies_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/mapped-in-ny-companies/depositor.py", task_id="depositor", dag=dag)

var_2015_green_taxi_trip_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2015-green-taxi-trip-data/depositor.py", task_id="depositor", dag=dag)

var_sea_level_rise_maps_2050s_500_year_floodplain_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sea-level-rise-maps-2050s-500-year-floodplain/depositor.py", task_id="depositor", dag=dag)

var_recycling_diversion_and_capture_rates_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/recycling-diversion-and-capture-rates/depositor.py", task_id="depositor", dag=dag)

var_nycha_facilities_and_service_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-facilities-and-service-centers/depositor.py", task_id="depositor", dag=dag)

var_citi_bike_live_station_feed_json_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citi-bike-live-station-feed-json/depositor.py", task_id="depositor", dag=dag)

var_citi_bike_live_station_feed_json_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citi-bike-live-station-feed-json/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_school_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-school-gender/depositor.py", task_id="depositor", dag=dag)

var_wholesale_markets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wholesale-markets/depositor.py", task_id="depositor", dag=dag)

var_energy_and_water_data_disclosure_for_local_law_84_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-and-water-data-disclosure-for-local-law-84-2011/depositor.py", task_id="depositor", dag=dag)

var_hero_banner_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hero-banner/depositor.py", task_id="depositor", dag=dag)

var_latin_media_organizations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/latin-media-organizations/depositor.py", task_id="depositor", dag=dag)

var_dob_cellular_antenna_filings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-cellular-antenna-filings/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_health_stat_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-health-stat/depositor.py", task_id="depositor", dag=dag)

var_neighborhood_names_gis_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/neighborhood-names-gis/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_investigations_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-investigations-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_street_pavement_rating_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-pavement-rating/depositor.py", task_id="depositor", dag=dag)

var_2001_campaign_payments_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2001-campaign-payments/depositor.py", task_id="depositor", dag=dag)

var_acs_community_partners_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acs-community-partners/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_brooklyn_north_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-brooklyn-north-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_election_district_poll_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/election-district-poll-sites/depositor.py", task_id="depositor", dag=dag)

var_school_progress_report_2009_2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-report-2009-2010/depositor.py", task_id="depositor", dag=dag)

var_park_closure_notifications_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/park-closure-notifications/depositor.py", task_id="depositor", dag=dag)

var_park_closure_notifications_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/park-closure-notifications/transform.py", task_id="transform", dag=dag)

var_dsny_solid_waste_management_freshkills_documents_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dsny-solid-waste-management-freshkills-documents/depositor.py", task_id="depositor", dag=dag)

var_gender_of_alleged_victims_compared_to_new_york_city_demographics_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/gender-of-alleged-victims-compared-to-new-york-city-demographics-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_projected_population_2010_2040_total_by_age_groups_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-population-2010-2040-total-by-age-groups/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_citywide_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-citywide-swd/depositor.py", task_id="depositor", dag=dag)

var_street_network_changes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-network-changes/depositor.py", task_id="depositor", dag=dag)

var_street_network_changes_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-network-changes/transform.py", task_id="transform", dag=dag)

var_transportation_structures_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/transportation-structures/depositor.py", task_id="depositor", dag=dag)

var_ccrb_average_days_for_the_ccrb_to_close_substantiated_cases_measured_from_date_of_incident_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-average-days-for-the-ccrb-to-close-substantiated-cases-measured-from-date-of-incident-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nycha_resident_jobs_programs_and_training_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-resident-jobs-programs-and-training/depositor.py", task_id="depositor", dag=dag)

var_energy_usage_from_dcas_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-usage-from-dcas-buildings/depositor.py", task_id="depositor", dag=dag)

var_ccrb_determinations_to_recommend_other_misconduct_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-determinations-to-recommend-other-misconduct-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_311_service_requests_for_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/311-service-requests-for-2008/depositor.py", task_id="depositor", dag=dag)

var_detention_and_placement_incident_reports_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/detention-and-placement-incident-reports/depositor.py", task_id="depositor", dag=dag)

var_detention_and_placement_incident_reports_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/detention-and-placement-incident-reports/transform.py", task_id="transform", dag=dag)

var_demographic_statistics_by_zip_code_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographic-statistics-by-zip-code/depositor.py", task_id="depositor", dag=dag)

var_directory_of_toilets_in_public_parks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-toilets-in-public-parks/depositor.py", task_id="depositor", dag=dag)

var_health_code_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/health-code/depositor.py", task_id="depositor", dag=dag)

var_police_department_disposition_of_substantiated_cases_by_year_of_ccrb_referral_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/police-department-disposition-of-substantiated-cases-by-year-of-ccrb-referral-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_revenue_budget_financial_plan_execadptprel_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/revenue-budget-financial-plan-execadptprel/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_full_time_positions_in_city_government_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-full-time-positions-in-city-government-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_manhattan_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-manhattan-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_lion_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lion/depositor.py", task_id="depositor", dag=dag)

var_lion_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lion/transform.py", task_id="transform", dag=dag)

var_dop_juvenile_violations_of_probation_filed_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-violations-of-probation-filed-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_athletic_facilities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/athletic-facilities/depositor.py", task_id="depositor", dag=dag)

var_building_complaint_disposition_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/building-complaint-disposition-codes/depositor.py", task_id="depositor", dag=dag)

var_nypd_complaint_data_historic_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nypd-complaint-data-historic/depositor.py", task_id="depositor", dag=dag)

var_neighborhood_tabulation_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/neighborhood-tabulation-areas/depositor.py", task_id="depositor", dag=dag)

var_empire_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/empire-zones/depositor.py", task_id="depositor", dag=dag)

var_2013_green_taxi_trip_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2013-green-taxi-trip-data/depositor.py", task_id="depositor", dag=dag)

var_census_demographics_at_the_nyc_city_council_district_cncld_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/census-demographics-at-the-nyc-city-council-district-cncld-level/depositor.py", task_id="depositor", dag=dag)

var_census_demographics_at_the_nyc_city_council_district_cncld_level_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/census-demographics-at-the-nyc-city-council-district-cncld-level/transform.py", task_id="transform", dag=dag)

var_new_york_state_mathematics_exam_by_school_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-state-mathematics-exam-by-school/depositor.py", task_id="depositor", dag=dag)

var_directory_of_land_use_application_fees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-land-use-application-fees/depositor.py", task_id="depositor", dag=dag)

var_capital_commitments_city_funds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capital-commitments-city-funds/depositor.py", task_id="depositor", dag=dag)

var_directory_of_hiking_trails_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-hiking-trails/depositor.py", task_id="depositor", dag=dag)

var_directory_of_hiking_trails_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-hiking-trails/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_citywide_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-citywide-all-students/depositor.py", task_id="depositor", dag=dag)

var_fdny_firehouse_listing_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-firehouse-listing/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_staten_island_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-staten-island/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_staten_island_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-staten-island/transform.py", task_id="transform", dag=dag)

var_nyc_domain_registrations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-domain-registrations/depositor.py", task_id="depositor", dag=dag)

var_replacement_projects_by_school_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/replacement-projects-by-school/depositor.py", task_id="depositor", dag=dag)

var_medicaid_income_levels_ages_65_and_up_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medicaid-income-levels-ages-65-and-up/depositor.py", task_id="depositor", dag=dag)

var_2009_campaign_payment_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2009-campaign-payment/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_beacon_satellite_at_nycha_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-beacon-satellite-at-nycha-programs/depositor.py", task_id="depositor", dag=dag)

var_where_incidents_that_led_to_a_complaint_took_place_by_precinct_queens_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-complaint-took-place-by-precinct-queens-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_in_queens_for_class_1_2_and_3_family_homes_2006_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2006/depositor.py", task_id="depositor", dag=dag)

var_property_address_directory_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-address-directory/depositor.py", task_id="depositor", dag=dag)

var_property_address_directory_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-address-directory/transform.py", task_id="transform", dag=dag)

var_doe_high_school_directory_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-directory-2016/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_rearrest_rate_monthly_average_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-rearrest-rate-monthly-average/depositor.py", task_id="depositor", dag=dag)

var_consumer_services_mediated_complaints_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/consumer-services-mediated-complaints/depositor.py", task_id="depositor", dag=dag)

var_directory_of_approved_tree_species_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-approved-tree-species-list/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_nne_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-nne/depositor.py", task_id="depositor", dag=dag)

var_2016_nyc_open_data_plan_list_of_datasets_removed_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2016-nyc-open-data-plan-list-of-datasets-removed/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_runaway_and_homeless_youth_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-runaway-and-homeless-youth/depositor.py", task_id="depositor", dag=dag)

var_special_event_concession_fee_details_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/special-event-concession-fee-details/depositor.py", task_id="depositor", dag=dag)

var_school_progress_reports_all_schools_2011_multiyear_summary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-reports-all-schools-2011-multiyear-summary/depositor.py", task_id="depositor", dag=dag)

var_location_information_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/location-information-report/depositor.py", task_id="depositor", dag=dag)

var_active_projects_under_construction_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/active-projects-under-construction/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nycha_norc_program_core_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nycha-norc-program-core-services/depositor.py", task_id="depositor", dag=dag)

var_city_council_legislative_items_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-council-legislative-items/depositor.py", task_id="depositor", dag=dag)

var_directory_of_boating_and_marinas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-boating-and-marinas/depositor.py", task_id="depositor", dag=dag)

var_directory_of_boating_and_marinas_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-boating-and-marinas/transform.py", task_id="transform", dag=dag)

var_graduation_outcomes_citywide_classes_of_2005_2011_total_cohort_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-citywide-classes-of-2005-2011-total-cohort/depositor.py", task_id="depositor", dag=dag)

var_nyc_street_centerline_cscl_for_plownyc_winter_201617_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-street-centerline-cscl-for-plownyc-winter-201617/depositor.py", task_id="depositor", dag=dag)

var_office_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/office-locations/depositor.py", task_id="depositor", dag=dag)

var_dob_license_fees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-license-fees/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_programs_2014_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-programs-2014-2015/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-drivers/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_drivers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-drivers/transform.py", task_id="transform", dag=dag)

var_ten_year_capital_strategy_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ten-year-capital-strategy/depositor.py", task_id="depositor", dag=dag)

var_fdny_important_phone_numbers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-important-phone-numbers/depositor.py", task_id="depositor", dag=dag)

var_directory_of_tennis_courts_with_online_registration_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-tennis-courts-with-online-registration/depositor.py", task_id="depositor", dag=dag)

var_directory_of_dog_runs_and_off_leash_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-dog-runs-and-off-leash-areas/depositor.py", task_id="depositor", dag=dag)

var_directory_of_dog_runs_and_off_leash_areas_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-dog-runs-and-off-leash-areas/transform.py", task_id="transform", dag=dag)

var_hydrography_structures_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hydrography-structures/depositor.py", task_id="depositor", dag=dag)

var_directory_of_cricket_fields_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-cricket-fields/depositor.py", task_id="depositor", dag=dag)

var_directory_of_cricket_fields_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-cricket-fields/transform.py", task_id="transform", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_citywide_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-citywide-by-gender/depositor.py", task_id="depositor", dag=dag)

var_ccrb_age_of_docket_measured_from_the_date_of_report_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-age-of-docket-measured-from-the-date-of-report-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_revenue_comps_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/revenue-comps/depositor.py", task_id="depositor", dag=dag)

var_business_improvement_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/business-improvement-districts/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_2010_2011_regents_based_mathela_apm_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-gender/depositor.py", task_id="depositor", dag=dag)

var_paratransit_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-drivers/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_discourtesy_allegations_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-discourtesy-allegations-2007/depositor.py", task_id="depositor", dag=dag)

var_directory_of_family_shelter_performance_ranking_fy_2012_q4_and_2013_q1_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-family-shelter-performance-ranking-fy-2012-q4-and-2013-q1/depositor.py", task_id="depositor", dag=dag)

var_emergency_food_assistance_program_quarterly_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/emergency-food-assistance-program-quarterly-report/depositor.py", task_id="depositor", dag=dag)

var_demographic_projection_report_enrollment_projections_new_york_city_public_schools_prepared_by_the_grier_partnership_part_c_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-the-grier-partnership-part-c/depositor.py", task_id="depositor", dag=dag)

var_montague_street_business_improvement_district_bid_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/montague-street-business-improvement-district-bid/depositor.py", task_id="depositor", dag=dag)

var_doe_building_space_usage_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-building-space-usage/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_population_by_census_tracts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-population-by-census-tracts/depositor.py", task_id="depositor", dag=dag)

var_transportable_classroom_units_buildings_only_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/transportable-classroom-units-buildings-only/depositor.py", task_id="depositor", dag=dag)

var_gender_of_officers_against_whom_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/gender-of-officers-against-whom-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_sidewalk_centerline_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk-centerline/depositor.py", task_id="depositor", dag=dag)

var_acceptable_double_check_valve_assemblies_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acceptable-double-check-valve-assemblies/depositor.py", task_id="depositor", dag=dag)

var_street_weekly_resurfacing_schedule_bronx_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-weekly-resurfacing-schedule-bronx/depositor.py", task_id="depositor", dag=dag)

var_historical_new_york_city_crime_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/historical-new-york-city-crime-data/depositor.py", task_id="depositor", dag=dag)

var_historical_new_york_city_crime_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/historical-new-york-city-crime-data/transform.py", task_id="transform", dag=dag)

var_disposition_of_discourtesy_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-discourtesy-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_state_assembly_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/state-assembly-districts/depositor.py", task_id="depositor", dag=dag)

var_primary_residential_zoning_by_lot_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/primary-residential-zoning-by-lot/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_other_patrol_services_bureau_commands_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-other-patrol-services-bureau-commands-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_wnw_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-wnw/depositor.py", task_id="depositor", dag=dag)

var_traffic_volume_counts_2011_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/traffic-volume-counts-2011-2012/depositor.py", task_id="depositor", dag=dag)

var_distribution_of_force_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/distribution-of-force-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_disciplinary_actions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disciplinary-actions/depositor.py", task_id="depositor", dag=dag)

var_2016_2017_school_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2016-2017-school-zones/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_violations_of_probation_disposed_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-violations-of-probation-disposed-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_activity_summary_of_lead_based_paint_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/activity-summary-of-lead-based-paint/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_bronx_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-bronx-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dep_cpr_data_from_july_2001_through_june_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-cpr-data-from-july-2001-through-june-2011/depositor.py", task_id="depositor", dag=dag)

var_2010_2011_class_size_citywide_summary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-2011-class-size-citywide-summary/depositor.py", task_id="depositor", dag=dag)

var_village_alliance_merchants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/village-alliance-merchants/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_manhattan_north_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-manhattan-north-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_fire_department_building_vacate_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-fire-department-building-vacate-list/depositor.py", task_id="depositor", dag=dag)

var_child_welfare_indicators_annual_and_quarterly_report_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/child-welfare-indicators-annual-and-quarterly-report-indicators/depositor.py", task_id="depositor", dag=dag)

var_child_welfare_indicators_annual_and_quarterly_report_indicators_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/child-welfare-indicators-annual-and-quarterly-report-indicators/transform.py", task_id="transform", dag=dag)

var_new_york_city_locations_providing_seasonal_flu_vaccinations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-locations-providing-seasonal-flu-vaccinations/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_school_level_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-school-level-by-gender/depositor.py", task_id="depositor", dag=dag)

var_spray_showers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/spray-showers/depositor.py", task_id="depositor", dag=dag)

var_facilities_database_facdb_supplemental_file_package_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/facilities-database-facdb-supplemental-file-package/depositor.py", task_id="depositor", dag=dag)

var_facilities_database_facdb_supplemental_file_package_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/facilities-database-facdb-supplemental-file-package/transform.py", task_id="transform", dag=dag)

var_dycd_contractors_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-contractors/depositor.py", task_id="depositor", dag=dag)

var_public_recycling_bins_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/public-recycling-bins/depositor.py", task_id="depositor", dag=dag)

var_small_purchase_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/small-purchase-report/depositor.py", task_id="depositor", dag=dag)

var_justice_scholars_organization_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/justice-scholars-organization-information/depositor.py", task_id="depositor", dag=dag)

var_nycha_citywide_special_events_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-citywide-special-events/depositor.py", task_id="depositor", dag=dag)

var_school_progress_reports_all_schools_2007_08_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-reports-all-schools-2007-08/depositor.py", task_id="depositor", dag=dag)

var_airport_polygon_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/airport-polygon/depositor.py", task_id="depositor", dag=dag)

var_wastewater_treatment_plant_performance_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wastewater-treatment-plant-performance-data/depositor.py", task_id="depositor", dag=dag)

var_wastewater_treatment_plant_performance_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wastewater-treatment-plant-performance-data/transform.py", task_id="transform", dag=dag)

var_outcome_of_preventive_cases_closed_by_borough_and_cd_cy_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/outcome-of-preventive-cases-closed-by-borough-and-cd-cy-2014/depositor.py", task_id="depositor", dag=dag)

var_outcome_of_preventive_cases_closed_by_borough_and_cd_cy_2014_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/outcome-of-preventive-cases-closed-by-borough-and-cd-cy-2014/transform.py", task_id="transform", dag=dag)

var_2010_census_tracts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-census-tracts/depositor.py", task_id="depositor", dag=dag)

var_ems_incident_dispatch_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ems-incident-dispatch-data/depositor.py", task_id="depositor", dag=dag)

var_buildings_subject_to_hpd_jurisdiction_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/buildings-subject-to-hpd-jurisdiction/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_case_closings_by_type_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-case-closings-by-type/depositor.py", task_id="depositor", dag=dag)

var_fy16_mmr_spending_and_budget_information_by_units_of_appropriation_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy16-mmr-spending-and-budget-information-by-units-of-appropriation/depositor.py", task_id="depositor", dag=dag)

var_hpd_other_city_financial_assistance_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-other-city-financial-assistance-element/depositor.py", task_id="depositor", dag=dag)

var_hiv_testing_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hiv-testing-locations/depositor.py", task_id="depositor", dag=dag)

var_medicaid_coverage_for_children_and_pregnant_women_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medicaid-coverage-for-children-and-pregnant-women-income-levels/depositor.py", task_id="depositor", dag=dag)

var_preferred_source_procurements_fy15_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/preferred-source-procurements-fy15/depositor.py", task_id="depositor", dag=dag)

var_nycha_development_data_book_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-development-data-book/depositor.py", task_id="depositor", dag=dag)

var_environmentally_preferable_purchasing_fy15_construction_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/environmentally-preferable-purchasing-fy15-construction/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_fatherhood_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-fatherhood/depositor.py", task_id="depositor", dag=dag)

var_school_demographics_and_accountability_snapshot_2006_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-demographics-and-accountability-snapshot-2006-2012/depositor.py", task_id="depositor", dag=dag)

var_2015_street_tree_census_tree_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2015-street-tree-census-tree-data/depositor.py", task_id="depositor", dag=dag)

var_city_owned_and_leased_property_local_law_48_of_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-owned-and-leased-property-local-law-48-of-2011/depositor.py", task_id="depositor", dag=dag)

var_tax_lien_sale_lists_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tax-lien-sale-lists/depositor.py", task_id="depositor", dag=dag)

var_election_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/election-districts/depositor.py", task_id="depositor", dag=dag)

var_zoning_map_index_section_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zoning-map-index-section/depositor.py", task_id="depositor", dag=dag)

var_doc_visitor_arrests_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doc-visitor-arrests/depositor.py", task_id="depositor", dag=dag)

var_school_progress_reports_all_schools_2006_07_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-reports-all-schools-2006-07/depositor.py", task_id="depositor", dag=dag)

var_city_marshals_revenue_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-marshals-revenue/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_queens_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-queens-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_steam_consumption_and_cost_2010_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/steam-consumption-and-cost-2010-2016/depositor.py", task_id="depositor", dag=dag)

var_drinking_fountains_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/drinking-fountains/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_violations_of_probation_filed_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-violations-of-probation-filed-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_prenatal_care_services_monthly_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/prenatal-care-services-monthly-income-levels/depositor.py", task_id="depositor", dag=dag)

var_linknyc_new_site_permit_applications_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/linknyc-new-site-permit-applications/depositor.py", task_id="depositor", dag=dag)

var_2000_census_blocks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2000-census-blocks/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_case_count_by_type_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-case-count-by-type/depositor.py", task_id="depositor", dag=dag)

var_new_york_public_library_nypl_branch_services_from_7_2010_to_6_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-public-library-nypl-branch-services-from-7-2010-to-6-2011/depositor.py", task_id="depositor", dag=dag)

var_sidewalk_café_licenses_and_applications_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk-café-licenses-and-applications/depositor.py", task_id="depositor", dag=dag)

var_fdny_line_of_duty_deaths_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-line-of-duty-deaths/depositor.py", task_id="depositor", dag=dag)

var_filming_locations_scenes_from_the_city_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/filming-locations-scenes-from-the-city/depositor.py", task_id="depositor", dag=dag)

var_filming_locations_scenes_from_the_city_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/filming-locations-scenes-from-the-city/transform.py", task_id="transform", dag=dag)

var_dop_juvenile_violations_of_probation_disposed_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-violations-of-probation-disposed-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_cases_snapshot_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-cases-snapshot-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_watershed_water_quality_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/watershed-water-quality-data/depositor.py", task_id="depositor", dag=dag)

var_capital_commitments_preladpt_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capital-commitments-preladpt/depositor.py", task_id="depositor", dag=dag)

var_dob_ecb_violations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-ecb-violations/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_queens_north_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-queens-north-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_supervision_passthrough_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-supervision-passthrough-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_community_health_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-health-centers/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2007/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2007_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2007/transform.py", task_id="transform", dag=dag)

var_full_time_and_full_time_equivalent_staffing_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/full-time-and-full-time-equivalent-staffing-levels/depositor.py", task_id="depositor", dag=dag)

var_map_of_nycha_community_facilities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/map-of-nycha-community-facilities/depositor.py", task_id="depositor", dag=dag)

var_columbus_avenue_bid_businesses_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/columbus-avenue-bid-businesses/depositor.py", task_id="depositor", dag=dag)

var_cancelled_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cancelled-projects/depositor.py", task_id="depositor", dag=dag)

var_nycha_application_frequently_asked_questions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-application-frequently-asked-questions/depositor.py", task_id="depositor", dag=dag)

var_parking_regulation_locations_and_signs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-regulation-locations-and-signs/depositor.py", task_id="depositor", dag=dag)

var_parking_regulation_locations_and_signs_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-regulation-locations-and-signs/transform.py", task_id="transform", dag=dag)

var_dof_condominium_comparable_rental_income_queens_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-queens-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_nyc_clean_heat_dataset_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-clean-heat-dataset/depositor.py", task_id="depositor", dag=dag)

var_credited_job_placement_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/credited-job-placement-report/depositor.py", task_id="depositor", dag=dag)

var_state_senate_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/state-senate-districts/depositor.py", task_id="depositor", dag=dag)

var_lower_manhattan_retailers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lower-manhattan-retailers/depositor.py", task_id="depositor", dag=dag)

var_drivers_and_attendants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/drivers-and-attendants/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_art_galleries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-art-galleries/depositor.py", task_id="depositor", dag=dag)

var_adult_medicaid_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/adult-medicaid-income-levels/depositor.py", task_id="depositor", dag=dag)

var_model_aircraft_fields_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/model-aircraft-fields/depositor.py", task_id="depositor", dag=dag)

var_acceptable_double_check_detector_assemblies_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acceptable-double-check-detector-assemblies/depositor.py", task_id="depositor", dag=dag)

var_1995_street_tree_census_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/1995-street-tree-census/depositor.py", task_id="depositor", dag=dag)

var_active_projects_infrastructure_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/active-projects-infrastructure/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_brooklyn_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-brooklyn-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_expense_financial_plan_adptprel_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-financial-plan-adptprel/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_school_level_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-school-level-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_bronx_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-bronx-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_brooklyn_north_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-brooklyn-north-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_vision_zero_base_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/vision-zero-base-report/depositor.py", task_id="depositor", dag=dag)

var_fdny_fire_department_fee_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-fire-department-fee/depositor.py", task_id="depositor", dag=dag)

var_board_of_education_1934_2002_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/board-of-education-1934-2002/depositor.py", task_id="depositor", dag=dag)

var_board_of_education_1934_2002_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/board-of-education-1934-2002/transform.py", task_id="transform", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_district_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-district-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_linknyc_usage_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/linknyc-usage-statistics/depositor.py", task_id="depositor", dag=dag)

var_school_spending_since_1990_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-spending-since-1990/depositor.py", task_id="depositor", dag=dag)

var_topographical_bureau_maps_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/topographical-bureau-maps/depositor.py", task_id="depositor", dag=dag)

var_times_square_signage_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-signage/depositor.py", task_id="depositor", dag=dag)

var_where_incidents_that_led_to_a_complaint_took_place_by_precinct_manhattan_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-complaint-took-place-by-precinct-manhattan-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_borough_classes_of_2005_2011_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-borough-classes-of-2005-2011-gender/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_2010_2011_regents_based_mathela_apm_total_cohort_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-total-cohort/depositor.py", task_id="depositor", dag=dag)

var_ccrb_age_of_docket_measured_from_the_date_of_incident_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-age-of-docket-measured-from-the-date-of-incident-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_future_construction_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-future-construction-projects/depositor.py", task_id="depositor", dag=dag)

var_fdny_community_board_incident_count_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-community-board-incident-count/depositor.py", task_id="depositor", dag=dag)

var_school_progress_report_2007_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-report-2007-2008/depositor.py", task_id="depositor", dag=dag)

var_invoices_for_open_market_order_omo_charges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/invoices-for-open-market-order-omo-charges/depositor.py", task_id="depositor", dag=dag)

var_fdny_repealed_rules_and_corresponding_new_fire_code_and_rules_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-repealed-rules-and-corresponding-new-fire-code-and-rules/depositor.py", task_id="depositor", dag=dag)

var_prek_vendors_by_transportation_site_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/prek-vendors-by-transportation-site/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_district_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-district-gender/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_citywide_classes_of_2005_2011_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-citywide-classes-of-2005-2011-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_medallion_taxi_initial_inspection_schedule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medallion-taxi-initial-inspection-schedule/depositor.py", task_id="depositor", dag=dag)

var_directory_of_concessions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-concessions/depositor.py", task_id="depositor", dag=dag)

var_directory_of_concessions_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-concessions/transform.py", task_id="transform", dag=dag)

var_graduation_outcomes_citywide_classes_of_2005_2011_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-citywide-classes-of-2005-2011-swd/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_queens_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-queens-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_staten_island_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-staten-island-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_school_progress_report_2010_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-report-2010-2011/depositor.py", task_id="depositor", dag=dag)

var_fire_incident_dispatch_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fire-incident-dispatch-data/depositor.py", task_id="depositor", dag=dag)

var_medical_assistance_program_medicaid_offices_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medical-assistance-program-medicaid-offices/depositor.py", task_id="depositor", dag=dag)

var_nyc_open_data_plan_list_of_datasets_removed_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-open-data-plan-list-of-datasets-removed/depositor.py", task_id="depositor", dag=dag)

var_neighborhood_development_area_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/neighborhood-development-area-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_medallion_drivers_historical_archive_372013_142014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medallion-drivers-historical-archive-372013-142014/depositor.py", task_id="depositor", dag=dag)

var_where_incidents_that_led_to_a_substantiated_complaint_took_place_brooklyn_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-substantiated-complaint-took-place-brooklyn-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_total_snap_recipients_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/total-snap-recipients/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_district_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-district-by-gender/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_force_allegations_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-force-allegations-2007/depositor.py", task_id="depositor", dag=dag)

var_housing_new_york_units_by_project_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/housing-new-york-units-by-project/depositor.py", task_id="depositor", dag=dag)

var_nyc_doe_2015_2016_final_class_size_report_pupil_to_teacher_ratio_ptr_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-doe-2015-2016-final-class-size-report-pupil-to-teacher-ratio-ptr/depositor.py", task_id="depositor", dag=dag)

var_doitt_classical_music_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doitt-classical-music/depositor.py", task_id="depositor", dag=dag)

var_waterfront_revitalization_program_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/waterfront-revitalization-program/depositor.py", task_id="depositor", dag=dag)

var_waterfront_revitalization_program_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/waterfront-revitalization-program/transform.py", task_id="transform", dag=dag)

var_for_hire_vehicles_fhv_active_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/for-hire-vehicles-fhv-active-drivers/depositor.py", task_id="depositor", dag=dag)

var_parking_violations_issued_fiscal_year_2014_august_2013_june_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-violations-issued-fiscal-year-2014-august-2013-june-2014/depositor.py", task_id="depositor", dag=dag)

var_directory_of_dhs_contacts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-dhs-contacts/depositor.py", task_id="depositor", dag=dag)

var_shelter_repair_scorecard_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/shelter-repair-scorecard/depositor.py", task_id="depositor", dag=dag)

var_for_hire_vehicle_fhv_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/for-hire-vehicle-fhv-drivers/depositor.py", task_id="depositor", dag=dag)

var_for_hire_vehicle_fhv_drivers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/for-hire-vehicle-fhv-drivers/transform.py", task_id="transform", dag=dag)

var_income_by_type_of_income_and_agi_range_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/income-by-type-of-income-and-agi-range/depositor.py", task_id="depositor", dag=dag)

var_school_safety_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-safety-report/depositor.py", task_id="depositor", dag=dag)

var_311_service_requests_for_2006_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/311-service-requests-for-2006/depositor.py", task_id="depositor", dag=dag)

var_directory_of_family_justice_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-family-justice-centers/depositor.py", task_id="depositor", dag=dag)

var_elevation_points_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/elevation-points/depositor.py", task_id="depositor", dag=dag)

var_tourism_grants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tourism-grants/depositor.py", task_id="depositor", dag=dag)

var_foil_report_trade_waste_all_approved_or_denied_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/foil-report-trade-waste-all-approved-or-denied/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_brokers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-brokers/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_brokers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-brokers/transform.py", task_id="transform", dag=dag)

var_dof_summary_of_neighborhood_sales_in_staten_island_for_class_1_2_and_3_family_homes_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-staten-island-for-class-1-2-and-3-family-homes-2008/depositor.py", task_id="depositor", dag=dag)

var_new_preventive_cases_opened_by_borough_and_cd_cy_15_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-preventive-cases-opened-by-borough-and-cd-cy-15/depositor.py", task_id="depositor", dag=dag)

var_new_preventive_cases_opened_by_borough_and_cd_cy_15_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-preventive-cases-opened-by-borough-and-cd-cy-15/transform.py", task_id="transform", dag=dag)

var_fdny_certificate_of_fitness_rules_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-certificate-of-fitness-rules-codes/depositor.py", task_id="depositor", dag=dag)

var_enrollment_capacity_and_utilization_reports_regular_hs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-regular-hs/depositor.py", task_id="depositor", dag=dag)

var_directory_of_tennis_courts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-tennis-courts/depositor.py", task_id="depositor", dag=dag)

var_directory_of_tennis_courts_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-tennis-courts/transform.py", task_id="transform", dag=dag)

var_charges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/charges/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_borough_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-borough-ell/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_watershed_statistics_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/watershed-statistics-2/depositor.py", task_id="depositor", dag=dag)

var_wirednyc_certified_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wirednyc-certified-buildings/depositor.py", task_id="depositor", dag=dag)

var_total_crime_index_for_the_nations_largest_cities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/total-crime-index-for-the-nations-largest-cities/depositor.py", task_id="depositor", dag=dag)

var_expense_financial_plan_exec_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-financial-plan-exec/depositor.py", task_id="depositor", dag=dag)

var_substantiated_officers_rank_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/substantiated-officers-rank/depositor.py", task_id="depositor", dag=dag)

var_construction_pipeline_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/construction-pipeline/depositor.py", task_id="depositor", dag=dag)

var_top_ten_elevator_offenders_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/top-ten-elevator-offenders/depositor.py", task_id="depositor", dag=dag)

var_nypd_complaint_data_current_ytd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nypd-complaint-data-current-ytd/depositor.py", task_id="depositor", dag=dag)

var_airport_point_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/airport-point/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_citywide_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-citywide-all-students/depositor.py", task_id="depositor", dag=dag)

var_pmmr_fy_2015_data_extract_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/pmmr-fy-2015-data-extract/depositor.py", task_id="depositor", dag=dag)

var_directory_of_horseback_riding_trails_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-horseback-riding-trails/depositor.py", task_id="depositor", dag=dag)

var_directory_of_horseback_riding_trails_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-horseback-riding-trails/transform.py", task_id="transform", dag=dag)

var_attendance_4pm_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/attendance-4pm-report/depositor.py", task_id="depositor", dag=dag)

var_enrollment_capacity_and_utilization_reports_historical_by_building_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-historical-by-building/depositor.py", task_id="depositor", dag=dag)

var_post_office_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/post-office/depositor.py", task_id="depositor", dag=dag)

var_nyc_openrecords_foil_request_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-openrecords-foil-request-data/depositor.py", task_id="depositor", dag=dag)

var_hpd_developer_selection_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-developer-selection-element/depositor.py", task_id="depositor", dag=dag)

var_list_of_cases_filed_by_type_at_oath_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/list-of-cases-filed-by-type-at-oath/depositor.py", task_id="depositor", dag=dag)

var_current_medallions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/current-medallions/depositor.py", task_id="depositor", dag=dag)

var_food_scrap_drop_off_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/food-scrap-drop-off-sites/depositor.py", task_id="depositor", dag=dag)

var_water_consumption_in_the_new_york_city_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/water-consumption-in-the-new-york-city/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_brooklyn_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-brooklyn-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_bike_routes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bike-routes/depositor.py", task_id="depositor", dag=dag)

var_2013_campaign_contributions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2013-campaign-contributions/depositor.py", task_id="depositor", dag=dag)

var_lcr_90th_percentile_dataset_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lcr-90th-percentile-dataset/depositor.py", task_id="depositor", dag=dag)

var_retaining_wall_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/retaining-wall/depositor.py", task_id="depositor", dag=dag)

var_community_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-districts/depositor.py", task_id="depositor", dag=dag)

var_social_indicators_report_data_by_community_district_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/social-indicators-report-data-by-community-district/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_citywide_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-citywide-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_nyc_civil_service_titles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-civil-service-titles/depositor.py", task_id="depositor", dag=dag)

var_civil_service_list_terminated_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/civil-service-list-terminated/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_supervision_intakes_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-supervision-intakes-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_investigations_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-investigations-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_public_pay_telephone_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/public-pay-telephone-locations/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_cases_snapshot_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-cases-snapshot-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_roadbed_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/roadbed/depositor.py", task_id="depositor", dag=dag)

var_nypl_branch_services_bronx_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nypl-branch-services-bronx/depositor.py", task_id="depositor", dag=dag)

var_2013_campaign_expenditures_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2013-campaign-expenditures/depositor.py", task_id="depositor", dag=dag)

var_sat_college_board_2010_school_level_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sat-college-board-2010-school-level-results/depositor.py", task_id="depositor", dag=dag)

var_museums_and_galleries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/museums-and-galleries/depositor.py", task_id="depositor", dag=dag)

var_museums_and_galleries_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/museums-and-galleries/transform.py", task_id="transform", dag=dag)

var_race_of_officers_against_whom_allegations_were_substantiated_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/race-of-officers-against-whom-allegations-were-substantiated/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_probationers_rearrested_as_a_percentage_of_nypd_arrest_report_monthly_average_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-probationers-rearrested-as-a-percentage-of-nypd-arrest-report-monthly-average/depositor.py", task_id="depositor", dag=dag)

var_pools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/pools/depositor.py", task_id="depositor", dag=dag)

var_2010_2011_class_size_district_level_distribution_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-2011-class-size-district-level-distribution/depositor.py", task_id="depositor", dag=dag)

var_community_board_applications_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-board-applications/depositor.py", task_id="depositor", dag=dag)

var_2016_nyc_open_data_plan_foil_reporting_metrics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2016-nyc-open-data-plan-foil-reporting-metrics/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_for_brooklyn_for_class_1_2_and_3_family_homes_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-for-brooklyn-for-class-1-2-and-3-family-homes-2009/depositor.py", task_id="depositor", dag=dag)

var_forestry_tree_points_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/forestry-tree-points/depositor.py", task_id="depositor", dag=dag)

var_izone_school_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/izone-school-list/depositor.py", task_id="depositor", dag=dag)

var_law_speeches_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/law-speeches/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_district_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-district-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_paratransit_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-bases/depositor.py", task_id="depositor", dag=dag)

var_ceps_organization_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ceps-organization-information/depositor.py", task_id="depositor", dag=dag)

var_odra_ma_trend_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/odra-ma-trend/depositor.py", task_id="depositor", dag=dag)

var_certified_asbestos_investigator_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/certified-asbestos-investigator/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_district_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-district-ell/depositor.py", task_id="depositor", dag=dag)

var_wirednyc_all_buildings_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wirednyc-all-buildings-data/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_allegations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-allegations/depositor.py", task_id="depositor", dag=dag)

var_school_progress_report_2008_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-report-2008-2009/depositor.py", task_id="depositor", dag=dag)

var_ccrb_age_of_substantiated_cases_measured_from_the_date_of_incident_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-age-of-substantiated-cases-measured-from-the-date-of-incident-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_district_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-district-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_colleges_and_universities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/colleges-and-universities/depositor.py", task_id="depositor", dag=dag)

var_hurricane_evacuation_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-evacuation-centers/depositor.py", task_id="depositor", dag=dag)

var_311_service_requests_for_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/311-service-requests-for-2009/depositor.py", task_id="depositor", dag=dag)

var_complaint_log_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/complaint-log/depositor.py", task_id="depositor", dag=dag)

var_dob_permit_issuance_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-permit-issuance/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_boro_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-boro-by-gender/depositor.py", task_id="depositor", dag=dag)

var_election_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/election-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_real_time_traffic_speed_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/real-time-traffic-speed-data/depositor.py", task_id="depositor", dag=dag)

var_real_time_traffic_speed_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/real-time-traffic-speed-data/transform.py", task_id="transform", dag=dag)

var_medallion_drivers_status_change_log_10282013_present_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medallion-drivers-status-change-log-10282013-present/depositor.py", task_id="depositor", dag=dag)

var_population_of_selected_asian_race_subgroups_in_new_york_city_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/population-of-selected-asian-race-subgroups-in-new-york-city-by-borough/depositor.py", task_id="depositor", dag=dag)

var_school_budget_overview_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-budget-overview/depositor.py", task_id="depositor", dag=dag)

var_2010_2011_class_size_district_level_summary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-2011-class-size-district-level-summary/depositor.py", task_id="depositor", dag=dag)

var_enforcement_fines_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enforcement-fines/depositor.py", task_id="depositor", dag=dag)

var_fy03_fy12_mmr_agency_performance_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy03-fy12-mmr-agency-performance-indicators/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_citywide_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_debt_outstanding_since_fy_2000_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-debt-outstanding-since-fy-2000/depositor.py", task_id="depositor", dag=dag)

var_summary_table_of_funding_sources_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/summary-table-of-funding-sources/depositor.py", task_id="depositor", dag=dag)

var_linknyc_locations_shapefile_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/linknyc-locations-shapefile/depositor.py", task_id="depositor", dag=dag)

var_procurement_by_method_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/procurement-by-method/depositor.py", task_id="depositor", dag=dag)

var_procurement_by_method_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/procurement-by-method/transform.py", task_id="transform", dag=dag)

var_foursquare_api_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/foursquare-api/depositor.py", task_id="depositor", dag=dag)

var_foursquare_api_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/foursquare-api/transform.py", task_id="transform", dag=dag)

var_dycd_after_school_programs_neighborhood_development_area_nda_family_support_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-neighborhood-development-area-nda-family-support/depositor.py", task_id="depositor", dag=dag)

var_adopt_a_tree_inventory_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/adopt-a-tree-inventory/depositor.py", task_id="depositor", dag=dag)

var_adopt_a_tree_inventory_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/adopt-a-tree-inventory/transform.py", task_id="transform", dag=dag)

var_fresh_food_stores_zoning_boundaries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fresh-food-stores-zoning-boundaries/depositor.py", task_id="depositor", dag=dag)

var_paratransit_services_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-services-vehicles/depositor.py", task_id="depositor", dag=dag)

var_paratransit_services_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-services-vehicles/transform.py", task_id="transform", dag=dag)

var_scenic_landmarks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/scenic-landmarks/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_borough_classes_of_2005_2011_total_cohort_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-borough-classes-of-2005-2011-total-cohort/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_citywide_classes_of_2005_2011_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-citywide-classes-of-2005-2011-gender/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_school_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-school-ell/depositor.py", task_id="depositor", dag=dag)

var_dep_cpr_critical_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-cpr-critical-indicators/depositor.py", task_id="depositor", dag=dag)

var_capacity_projects_by_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capacity-projects-by-schools/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_investigations_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-investigations-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_new_york_citys_school_age_and_65_and_over_populations_by_borough_1950_2040_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-citys-school-age-and-65-and-over-populations-by-borough-1950-2040/depositor.py", task_id="depositor", dag=dag)

var_ccrb_age_of_victims_whose_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-age-of-victims-whose-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_district_by_disability_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-district-by-disability-status/depositor.py", task_id="depositor", dag=dag)

var_current_plan_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/current-plan-programs/depositor.py", task_id="depositor", dag=dag)

var_dcla_cultural_institutions_group_funding_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-cultural-institutions-group-funding/depositor.py", task_id="depositor", dag=dag)

var_chancellor_of_nyc_board_of_education_1970_1989_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/chancellor-of-nyc-board-of-education-1970-1989/depositor.py", task_id="depositor", dag=dag)

var_chancellor_of_nyc_board_of_education_1970_1989_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/chancellor-of-nyc-board-of-education-1970-1989/transform.py", task_id="transform", dag=dag)

var_dof_cooperative_comparable_rental_income_staten_island_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-staten-island-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_times_square_screens_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-screens/depositor.py", task_id="depositor", dag=dag)

var_ccrb_command_rankings_complaints_per_uniformed_officer_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-command-rankings-complaints-per-uniformed-officer-2009/depositor.py", task_id="depositor", dag=dag)

var_tax_credits_by_agi_range_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tax-credits-by-agi-range/depositor.py", task_id="depositor", dag=dag)

var_added_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/added-projects/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_family_support_programs_for_seniors_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-family-support-programs-for-seniors/depositor.py", task_id="depositor", dag=dag)

var_agency_service_center_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/agency-service-center/depositor.py", task_id="depositor", dag=dag)

var_community_health_survey_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-health-survey/depositor.py", task_id="depositor", dag=dag)

var_directory_of_food_stamp_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-food-stamp-centers/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_agents_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-agents/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_agents_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-agents/transform.py", task_id="transform", dag=dag)

var_boardwalk_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/boardwalk/depositor.py", task_id="depositor", dag=dag)

var_dcla_cultural_organizations_capital_funding_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-cultural-organizations-capital-funding/depositor.py", task_id="depositor", dag=dag)

var_race_of_victims_whose_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/race-of-victims-whose-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_service_hotlines_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-service-hotlines/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_district_by_disability_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-district-by-disability-status/depositor.py", task_id="depositor", dag=dag)

var_hose_nozzle_and_sprayer_survey_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hose-nozzle-and-sprayer-survey/depositor.py", task_id="depositor", dag=dag)

var_commuter_van_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/commuter-van-vehicles/depositor.py", task_id="depositor", dag=dag)

var_administrative_code_18_144_park_maintenance_report_payroll_data_fiscal_year_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/administrative-code-18-144-park-maintenance-report-payroll-data-fiscal-year-2016/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_other_bureaus_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-other-bureaus-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_weekly_resurfacing_schedule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weekly-resurfacing-schedule/depositor.py", task_id="depositor", dag=dag)

var_weekly_resurfacing_schedule_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weekly-resurfacing-schedule/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_boro_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-boro-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_privately_owned_public_spaces_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/privately-owned-public-spaces/depositor.py", task_id="depositor", dag=dag)

var_privately_owned_public_spaces_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/privately-owned-public-spaces/transform.py", task_id="transform", dag=dag)

var_bicycle_shelters_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bicycle-shelters/depositor.py", task_id="depositor", dag=dag)

var_bicycle_shelters_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bicycle-shelters/transform.py", task_id="transform", dag=dag)

var_nypl_branch_services_manhattan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nypl-branch-services-manhattan/depositor.py", task_id="depositor", dag=dag)

var_city_owned_and_leased_property_colp_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-owned-and-leased-property-colp/depositor.py", task_id="depositor", dag=dag)

var_city_owned_and_leased_property_colp_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-owned-and-leased-property-colp/transform.py", task_id="transform", dag=dag)

var_municipal_parking_facilities_queens_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-queens/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_queens_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-queens/transform.py", task_id="transform", dag=dag)

var_new_york_city_leading_causes_of_death_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-leading-causes-of-death/depositor.py", task_id="depositor", dag=dag)

var_dataset_nominations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dataset-nominations/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_boroughs_and_other_commands_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-boroughs-and-other-commands-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_street_hail_livery_shl_taxi_initial_inspection_schedule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-hail-livery-shl-taxi-initial-inspection-schedule/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_staten_island_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-staten-island-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_bike_counts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bike-counts/depositor.py", task_id="depositor", dag=dag)

var_bike_counts_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bike-counts/transform.py", task_id="transform", dag=dag)

var_where_incidents_that_led_to_a_substantiated_complaint_took_place_staten_island_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-substantiated-complaint-took-place-staten-island-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_adult_shelter_performance_ranking_fy_2011_q3_2011_q4_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-adult-shelter-performance-ranking-fy-2011-q3-2011-q4/depositor.py", task_id="depositor", dag=dag)

var_2015_2016_school_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2015-2016-school-zones/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_force_allegations_2005_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-force-allegations-2005/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_boro_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-boro-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_primary_manufacturing_zoning_by_lot_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/primary-manufacturing-zoning-by-lot/depositor.py", task_id="depositor", dag=dag)

var_family_adult_court_contact_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/family-adult-court-contact-information/depositor.py", task_id="depositor", dag=dag)

var_congressional_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/congressional-districts/depositor.py", task_id="depositor", dag=dag)

var_federal_stimulus_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/federal-stimulus-data/depositor.py", task_id="depositor", dag=dag)

var_paratransit_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-vehicles/depositor.py", task_id="depositor", dag=dag)

var_state_assembly_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/state-assembly-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_reservoir_characteristics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/reservoir-characteristics/depositor.py", task_id="depositor", dag=dag)

var_list_of_translation_services_provided_at_oath_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/list-of-translation-services-provided-at-oath/depositor.py", task_id="depositor", dag=dag)

var_dhs_daily_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dhs-daily-report/depositor.py", task_id="depositor", dag=dag)

var_tlc_community_car_service_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tlc-community-car-service-bases/depositor.py", task_id="depositor", dag=dag)

var_tlc_vehicle_insurance_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tlc-vehicle-insurance/depositor.py", task_id="depositor", dag=dag)

var_new_york_tech_ecosystem_report_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-tech-ecosystem-report-data/depositor.py", task_id="depositor", dag=dag)

var_new_york_tech_ecosystem_report_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-tech-ecosystem-report-data/transform.py", task_id="transform", dag=dag)

var_ged_plus_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ged-plus-locations/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_citywide_by_disability_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-citywide-by-disability-status/depositor.py", task_id="depositor", dag=dag)

var_hpd_lihtc_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-lihtc-element/depositor.py", task_id="depositor", dag=dag)

var_dsnys_refuse_and_recycling_disposal_networks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dsnys-refuse-and-recycling-disposal-networks/depositor.py", task_id="depositor", dag=dag)

var_routes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/routes/depositor.py", task_id="depositor", dag=dag)

var_additional_revenue_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/additional-revenue/depositor.py", task_id="depositor", dag=dag)

var_facilities_database_shapefile_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/facilities-database-shapefile/depositor.py", task_id="depositor", dag=dag)

var_school_attendance_and_enrollment_by_district_2010_11_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-attendance-and-enrollment-by-district-2010-11/depositor.py", task_id="depositor", dag=dag)

var_nypl_branch_services_staten_island_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nypl-branch-services-staten-island/depositor.py", task_id="depositor", dag=dag)

var_health_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/health-areas/depositor.py", task_id="depositor", dag=dag)

var_empower_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/empower-zones/depositor.py", task_id="depositor", dag=dag)

var_atomic_polygons_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/atomic-polygons/depositor.py", task_id="depositor", dag=dag)

var_sidewalk_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk/depositor.py", task_id="depositor", dag=dag)

var_financial_empowerment_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/financial-empowerment-centers/depositor.py", task_id="depositor", dag=dag)

var_2010_school_survey_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-school-survey/depositor.py", task_id="depositor", dag=dag)

var_2010_school_survey_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-school-survey/transform.py", task_id="transform", dag=dag)

var_ccrb_age_of_alleged_victims_compared_to_new_york_city_demographics_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-age-of-alleged-victims-compared-to-new-york-city-demographics-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_commissioners_regulations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/commissioners-regulations/depositor.py", task_id="depositor", dag=dag)

var_community_parks_initiative_zone_boundaries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-parks-initiative-zone-boundaries/depositor.py", task_id="depositor", dag=dag)

var_nyc_department_of_education_job_titles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-department-of-education-job-titles/depositor.py", task_id="depositor", dag=dag)

var_universal_pre_k_upk_school_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/universal-pre-k-upk-school-locations/depositor.py", task_id="depositor", dag=dag)

var_shl_vehicles_authorized_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/shl-vehicles-authorized/depositor.py", task_id="depositor", dag=dag)

var_expense_budget_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-budget/depositor.py", task_id="depositor", dag=dag)

var_latin_cultural_organizations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/latin-cultural-organizations/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_staten_island_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-staten-island-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_nyc_greenthumb_community_gardens_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-greenthumb-community-gardens/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_non_tax_revenues_fy_1980_fy_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-non-tax-revenues-fy-1980-fy-2013/depositor.py", task_id="depositor", dag=dag)

var_nyc_truck_routes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-truck-routes/depositor.py", task_id="depositor", dag=dag)

var_nyc_truck_routes_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-truck-routes/transform.py", task_id="transform", dag=dag)

var_participatory_budgeting_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/participatory-budgeting-projects/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_brooklyn_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-brooklyn/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_brooklyn_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-brooklyn/transform.py", task_id="transform", dag=dag)

var_individual_landmarks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/individual-landmarks/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_early_discharges_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-early-discharges-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_cooling_tower_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cooling-tower/depositor.py", task_id="depositor", dag=dag)

var_projected_population_2010_2040_males_by_age_groups_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-population-2010-2040-males-by-age-groups/depositor.py", task_id="depositor", dag=dag)

var_fire_alarms_periodic_inspection_testing_requirements_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fire-alarms-periodic-inspection-testing-requirements/depositor.py", task_id="depositor", dag=dag)

var_housing_new_york_units_by_building_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/housing-new-york-units-by-building/depositor.py", task_id="depositor", dag=dag)

var_2000_census_tracts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2000-census-tracts/depositor.py", task_id="depositor", dag=dag)

var_alerts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/alerts/depositor.py", task_id="depositor", dag=dag)

var_publicly_accessible_waterfront_spaces_paws_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/publicly-accessible-waterfront-spaces-paws/depositor.py", task_id="depositor", dag=dag)

var_total_housing_units_by_occupancy_status_and_tenure_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/total-housing-units-by-occupancy-status-and-tenure-by-borough/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_manhattan_south_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-manhattan-south-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_oil_usage_select_city_owned_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/oil-usage-select-city-owned-buildings/depositor.py", task_id="depositor", dag=dag)

var_advanced_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/advanced-projects/depositor.py", task_id="depositor", dag=dag)

var_expense_city_funds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-city-funds/depositor.py", task_id="depositor", dag=dag)

var_nyc_jobs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-jobs/depositor.py", task_id="depositor", dag=dag)

var_zip_code_boundaries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zip-code-boundaries/depositor.py", task_id="depositor", dag=dag)

var_zip_code_boundaries_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zip-code-boundaries/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_charter_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-charter-schools/depositor.py", task_id="depositor", dag=dag)

var_sustainability_indicators_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sustainability-indicators-2012/depositor.py", task_id="depositor", dag=dag)

var_nycha_customer_contact_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-customer-contact-centers/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_rearrest_rate_monthly_average_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-rearrest-rate-monthly-average/depositor.py", task_id="depositor", dag=dag)

var_statistical_forecasting_demographic_projection_report_enrollment_projections_new_york_city_public_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/statistical-forecasting-demographic-projection-report-enrollment-projections-new-york-city-public-schools/depositor.py", task_id="depositor", dag=dag)

var_communities_potentially_eligible_for_community_wastewater_management_program_funds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/communities-potentially-eligible-for-community-wastewater-management-program-funds/depositor.py", task_id="depositor", dag=dag)

var_court_liaison_contact_sheet_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/court-liaison-contact-sheet/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2008_general_education_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2008-general-education/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2008_general_education_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2008-general-education/transform.py", task_id="transform", dag=dag)

var_school_point_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-point-locations/depositor.py", task_id="depositor", dag=dag)

var_school_point_locations_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-point-locations/transform.py", task_id="transform", dag=dag)

var_reasons_for_police_civilian_encounters_that_led_to_a_complaint_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/reasons-for-police-civilian-encounters-that-led-to-a-complaint-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_mwbe_lbe_and_ebe_certified_business_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/mwbe-lbe-and-ebe-certified-business-list/depositor.py", task_id="depositor", dag=dag)

var_2009_campaign_contributions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2009-campaign-contributions/depositor.py", task_id="depositor", dag=dag)

var_civil_service_list_certification_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/civil-service-list-certification/depositor.py", task_id="depositor", dag=dag)

var_union_square_partnership_usp_business_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/union-square-partnership-usp-business-list/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_2010_2011_regents_based_mathela_apm_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-ell/depositor.py", task_id="depositor", dag=dag)

var_franchise_and_concession_review_committee_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/franchise-and-concession-review-committee/depositor.py", task_id="depositor", dag=dag)

var_franchise_and_concession_review_committee_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/franchise-and-concession-review-committee/transform.py", task_id="transform", dag=dag)

var_observations_and_statuses_for_inspections_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/observations-and-statuses-for-inspections/depositor.py", task_id="depositor", dag=dag)

var_safety_net_assistance_sna_recipients_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/safety-net-assistance-sna-recipients/depositor.py", task_id="depositor", dag=dag)

var_expense_budget_funding_all_source_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-budget-funding-all-source/depositor.py", task_id="depositor", dag=dag)

var_city_council_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-council-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_abuseneglect_by_community_district_cd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/abuseneglect-by-community-district-cd/depositor.py", task_id="depositor", dag=dag)

var_abuseneglect_by_community_district_cd_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/abuseneglect-by-community-district-cd/transform.py", task_id="transform", dag=dag)

var_times_square_food_beverage_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-food-beverage-locations/depositor.py", task_id="depositor", dag=dag)

var_landfills_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/landfills/depositor.py", task_id="depositor", dag=dag)

var_acris_document_control_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acris-document-control-codes/depositor.py", task_id="depositor", dag=dag)

var_social_indicators_report_data_citywide_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/social-indicators-report-data-citywide/depositor.py", task_id="depositor", dag=dag)

var_study_material_for_certificate_of_fitness_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/study-material-for-certificate-of-fitness/depositor.py", task_id="depositor", dag=dag)

var_open_balance_manhattan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-balance-manhattan/depositor.py", task_id="depositor", dag=dag)

var_open_balance_manhattan_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-balance-manhattan/transform.py", task_id="transform", dag=dag)

var_nyc_school_survey_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2011/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2011_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2011/transform.py", task_id="transform", dag=dag)

var_enrollment_capacity_and_utilization_reports_historical_by_organization_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-historical-by-organization/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_borough_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-borough-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_constituent_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/constituent-services/depositor.py", task_id="depositor", dag=dag)

var_nycdcp_manhattan_bike_count_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycdcp-manhattan-bike-count-locations/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_of_2005_2011_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-of-2005-2011-swd/depositor.py", task_id="depositor", dag=dag)

var_fhv_base_aggregate_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fhv-base-aggregate-report/depositor.py", task_id="depositor", dag=dag)

var_fy_2017_pmmr_data_extract_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy-2017-pmmr-data-extract/depositor.py", task_id="depositor", dag=dag)

var_city_council_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-council-districts/depositor.py", task_id="depositor", dag=dag)

var_fire_battalions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fire-battalions/depositor.py", task_id="depositor", dag=dag)

var_mobile_telecommunication_franchise_poletop_installation_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/mobile-telecommunication-franchise-poletop-installation-locations/depositor.py", task_id="depositor", dag=dag)

var_daily_report_of_single_adult_and_family_intake_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/daily-report-of-single-adult-and-family-intake/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_boro_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-boro-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_new_driver_application_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-driver-application-status/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_district_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-district-swd/depositor.py", task_id="depositor", dag=dag)

var_placements_by_community_district_cd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/placements-by-community-district-cd/depositor.py", task_id="depositor", dag=dag)

var_placements_by_community_district_cd_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/placements-by-community-district-cd/transform.py", task_id="transform", dag=dag)

var_shl_vehicles_lpep_provider_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/shl-vehicles-lpep-provider/depositor.py", task_id="depositor", dag=dag)

var_dycd_literacy_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-literacy/depositor.py", task_id="depositor", dag=dag)

var_dsny_special_waste_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dsny-special-waste/depositor.py", task_id="depositor", dag=dag)

var_ccrb_average_days_for_the_police_department_to_close_substantiated_ccrb_cases_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-average-days-for-the-police-department-to-close-substantiated-ccrb-cases-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_inmate_assault_on_staff_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-assault-on-staff/depositor.py", task_id="depositor", dag=dag)

var_inmate_arrests_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-arrests/depositor.py", task_id="depositor", dag=dag)

var_selected_facilities_and_program_sites_text_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/selected-facilities-and-program-sites-text/depositor.py", task_id="depositor", dag=dag)

var_selected_facilities_and_program_sites_text_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/selected-facilities-and-program-sites-text/transform.py", task_id="transform", dag=dag)

var_yellow_medallion_taxicabs_metershops_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-metershops/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_metershops_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-metershops/transform.py", task_id="transform", dag=dag)

var_math_test_results_2006_2012_borough_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-borough-all-students/depositor.py", task_id="depositor", dag=dag)

var_doc_annual_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doc-annual-statistics/depositor.py", task_id="depositor", dag=dag)

var_denied_registrants_in_the_wholesale_markets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/denied-registrants-in-the-wholesale-markets/depositor.py", task_id="depositor", dag=dag)

var_average_daily_inmate_population_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/average-daily-inmate-population/depositor.py", task_id="depositor", dag=dag)

var_nyc_reach_members_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-reach-members/depositor.py", task_id="depositor", dag=dag)

var_demographics_and_profiles_at_the_neighborhood_tabulation_area_nta_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographics-and-profiles-at-the-neighborhood-tabulation-area-nta-level/depositor.py", task_id="depositor", dag=dag)

var_demographics_and_profiles_at_the_neighborhood_tabulation_area_nta_level_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographics-and-profiles-at-the-neighborhood-tabulation-area-nta-level/transform.py", task_id="transform", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_detective_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-detective-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dob_sign_application_filings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-sign-application-filings/depositor.py", task_id="depositor", dag=dag)

var_commuter_van_services_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/commuter-van-services-vehicles/depositor.py", task_id="depositor", dag=dag)

var_commuter_van_services_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/commuter-van-services-vehicles/transform.py", task_id="transform", dag=dag)

var_dcas_managed_building_energy_usage_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcas-managed-building-energy-usage/depositor.py", task_id="depositor", dag=dag)

var_special_traffic_updates_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/special-traffic-updates/depositor.py", task_id="depositor", dag=dag)

var_special_traffic_updates_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/special-traffic-updates/transform.py", task_id="transform", dag=dag)

var_gender_of_victims_whose_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/gender-of-victims-whose-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_community_car_service_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-car-service-vehicles/depositor.py", task_id="depositor", dag=dag)

var_licensing_center_customer_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/licensing-center-customer-information/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_borough_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-borough-swd/depositor.py", task_id="depositor", dag=dag)

var_greenbook_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/greenbook/depositor.py", task_id="depositor", dag=dag)

var_how_complaints_filed_with_the_ccrb_were_reported_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/how-complaints-filed-with-the-ccrb-were-reported-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_patient_population_at_world_trade_center_wtc_environmental_health_center_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/patient-population-at-world-trade-center-wtc-environmental-health-center/depositor.py", task_id="depositor", dag=dag)

var_dob_now_build_job_application_filings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-now-build-job-application-filings/depositor.py", task_id="depositor", dag=dag)

var_dycd_osy_out_of_school_youth_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-osy-out-of-school-youth/depositor.py", task_id="depositor", dag=dag)

var_city_owned_and_leased_property_colp_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-owned-and-leased-property-colp-2/depositor.py", task_id="depositor", dag=dag)

var_ceqr_project_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ceqr-project-locations/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_citywide_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-all-students/depositor.py", task_id="depositor", dag=dag)

var_vehicle_classification_counts_2011_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/vehicle-classification-counts-2011-2012/depositor.py", task_id="depositor", dag=dag)

var_dcla_programs_funding_for_fy2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-programs-funding-for-fy2010/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_school_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-school-all-students/depositor.py", task_id="depositor", dag=dag)

var_nyc_parks_public_events_upcoming_14_days_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-parks-public-events-upcoming-14-days/depositor.py", task_id="depositor", dag=dag)

var_nyc_parks_public_events_upcoming_14_days_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-parks-public-events-upcoming-14-days/transform.py", task_id="transform", dag=dag)

var_concretehardware_weekly_repair_schedule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/concretehardware-weekly-repair-schedule/depositor.py", task_id="depositor", dag=dag)

var_rank_of_subject_officers_against_whom_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/rank-of-subject-officers-against-whom-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_borough_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-borough-all-students/depositor.py", task_id="depositor", dag=dag)

var_directory_of_dop_office_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-dop-office-locations/depositor.py", task_id="depositor", dag=dag)

var_fdny_fire_rule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-fire-rule/depositor.py", task_id="depositor", dag=dag)

var_nyc_permitted_event_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-permitted-event-information/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_for_the_bronx_for_class_1_2_and_3_family_homes_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-for-the-bronx-for-class-1-2-and-3-family-homes-2009/depositor.py", task_id="depositor", dag=dag)

var_medallion_drivers_active_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medallion-drivers-active/depositor.py", task_id="depositor", dag=dag)

var_coursestraining_provider_listing_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/coursestraining-provider-listing/depositor.py", task_id="depositor", dag=dag)

var_dep_green_infrastructure_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-green-infrastructure/depositor.py", task_id="depositor", dag=dag)

var_dep_green_infrastructure_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-green-infrastructure/transform.py", task_id="transform", dag=dag)

var_dop_juvenile_investigations_assigned_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-investigations-assigned/depositor.py", task_id="depositor", dag=dag)

var_annual_report_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annual-report-statistics/depositor.py", task_id="depositor", dag=dag)

var_annual_report_statistics_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annual-report-statistics/transform.py", task_id="transform", dag=dag)

var_doe_high_school_programs_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-programs-2016/depositor.py", task_id="depositor", dag=dag)

var_office_of_adult_and_continuing_education_location_directory_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/office-of-adult-and-continuing-education-location-directory/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_for_staten_island_for_class_1_2_and_3_family_homes_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-for-staten-island-for-class-1-2-and-3-family-homes-2009/depositor.py", task_id="depositor", dag=dag)

var_method_of_filing_complaint_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/method-of-filing-complaint/depositor.py", task_id="depositor", dag=dag)

var_311_service_requests_from_2010_to_present_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/311-service-requests-from-2010-to-present/depositor.py", task_id="depositor", dag=dag)

var_health_and_human_services_prequalification_catalog_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/health-and-human-services-prequalification-catalog/depositor.py", task_id="depositor", dag=dag)

var_street_hail_livery_shl_drivers_active_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-hail-livery-shl-drivers-active/depositor.py", task_id="depositor", dag=dag)

var_congress_district_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/congress-district-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_performance_directory_2013_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-performance-directory-2013-2014/depositor.py", task_id="depositor", dag=dag)

var_state_senate_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/state-senate-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_zip_code_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zip-code-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_force_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-force-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_early_discharges_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-early-discharges-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_lincoln_square_bid_business_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lincoln-square-bid-business-list/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_the_housing_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-the-housing-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_grier_partnership_part_b_demographic_projection_report_enrollment_projections_new_york_city_public_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/grier-partnership-part-b-demographic-projection-report-enrollment-projections-new-york-city-public-schools/depositor.py", task_id="depositor", dag=dag)

var_parking_violations_issued_fiscal_year_2017_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-violations-issued-fiscal-year-2017/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_street_reconstruction_10_year_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-street-reconstruction-10-year-plan/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_street_reconstruction_10_year_plan_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-street-reconstruction-10-year-plan/transform.py", task_id="transform", dag=dag)

var_311_service_requests_for_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/311-service-requests-for-2007/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_water_trail_kayak_and_canoe_launch_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-water-trail-kayak-and-canoe-launch-sites/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_water_trail_kayak_and_canoe_launch_sites_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-water-trail-kayak-and-canoe-launch-sites/transform.py", task_id="transform", dag=dag)

var_citywide_low_bridges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citywide-low-bridges/depositor.py", task_id="depositor", dag=dag)

var_citywide_low_bridges_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citywide-low-bridges/transform.py", task_id="transform", dag=dag)

var_dop_adult_violations_of_probation_disposed_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-violations-of-probation-disposed-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_shl_vehicle_endorsed_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/shl-vehicle-endorsed-bases/depositor.py", task_id="depositor", dag=dag)

var_2003_campaign_payments_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2003-campaign-payments/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_manhattan_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-manhattan-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_milliontreesnyc_forest_restoration_planting_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/milliontreesnyc-forest-restoration-planting-sites/depositor.py", task_id="depositor", dag=dag)

var_milliontreesnyc_block_planting_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/milliontreesnyc-block-planting-locations/depositor.py", task_id="depositor", dag=dag)

var_directory_of_public_computer_resource_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-public-computer-resource-centers/depositor.py", task_id="depositor", dag=dag)

var_directory_of_public_computer_resource_centers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-public-computer-resource-centers/transform.py", task_id="transform", dag=dag)

var_rate_at_which_the_ccrb_made_findings_on_the_merits_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/rate-at-which-the-ccrb-made-findings-on-the-merits-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dep_bureau_of_wastewater_treatment_bwt_2011_nuisance_complaints_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dep-bureau-of-wastewater-treatment-bwt-2011-nuisance-complaints/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_abuse_of_authority_allegations_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-abuse-of-authority-allegations-2008/depositor.py", task_id="depositor", dag=dag)

var_trade_waste_hauler_licensees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/trade-waste-hauler-licensees/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_citywide_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-citywide-ell/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_queens_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-queens-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_abuse_of_authority_allegations_2006_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-abuse-of-authority-allegations-2006/depositor.py", task_id="depositor", dag=dag)

var_ccr_annual_report_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccr-annual-report-2/depositor.py", task_id="depositor", dag=dag)

var_ccr_annual_report_2_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccr-annual-report-2/transform.py", task_id="transform", dag=dag)

var_dof_cooperative_comparable_rental_income_brooklyn_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-brooklyn-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_borough_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-borough-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_staten_island_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-staten-island-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_aging_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/aging-services/depositor.py", task_id="depositor", dag=dag)

var_2007_08_class_size_school_level_detail_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2007-08-class-size-school-level-detail/depositor.py", task_id="depositor", dag=dag)

var_young_adult_borough_centers_2012_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/young-adult-borough-centers-2012-2013/depositor.py", task_id="depositor", dag=dag)

var_construction_demoliton_registrants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/construction-demoliton-registrants/depositor.py", task_id="depositor", dag=dag)

var_nyccas_air_pollution_rasters_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyccas-air-pollution-rasters/depositor.py", task_id="depositor", dag=dag)

var_nyccas_air_pollution_rasters_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyccas-air-pollution-rasters/transform.py", task_id="transform", dag=dag)

var_capital_project_schedules_and_budgets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capital-project-schedules-and-budgets/depositor.py", task_id="depositor", dag=dag)

var_wastewater_treatment_plant_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wastewater-treatment-plant-data/depositor.py", task_id="depositor", dag=dag)

var_2016_green_taxi_trip_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2016-green-taxi-trip-data/depositor.py", task_id="depositor", dag=dag)

var_2010_2011_class_size_borough_summary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-2011-class-size-borough-summary/depositor.py", task_id="depositor", dag=dag)

var_dfta_contracts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dfta-contracts/depositor.py", task_id="depositor", dag=dag)

var_property_data_buildings_information_system_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-data-buildings-information-system/depositor.py", task_id="depositor", dag=dag)

var_assessment_actions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/assessment-actions/depositor.py", task_id="depositor", dag=dag)

var_controllable_agency_expenses_financial_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/controllable-agency-expenses-financial-plan/depositor.py", task_id="depositor", dag=dag)

var_hra_facts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hra-facts/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_manhattan_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-manhattan-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_path_line_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/path-line/depositor.py", task_id="depositor", dag=dag)

var_nyc_domain_registrations_by_zip_code_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-domain-registrations-by-zip-code/depositor.py", task_id="depositor", dag=dag)

var_nyc_social_media_usage_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-social-media-usage/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_boro_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-boro-by-gender/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_school_level_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-school-level-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_points_of_interest_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/points-of-interest/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_violations_of_probation_disposed_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-violations-of-probation-disposed-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_2014_2015_school_quality_reports_results_for_high_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-2015-school-quality-reports-results-for-high-schools/depositor.py", task_id="depositor", dag=dag)

var_2014_2015_school_quality_reports_results_for_high_schools_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-2015-school-quality-reports-results-for-high-schools/transform.py", task_id="transform", dag=dag)

var_school_progress_report_2006_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-report-2006-2007/depositor.py", task_id="depositor", dag=dag)

var_dsny_graffiti_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dsny-graffiti-information/depositor.py", task_id="depositor", dag=dag)

var_parks_properties_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parks-properties/depositor.py", task_id="depositor", dag=dag)

var_directory_of_temporary_public_art_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-temporary-public-art/depositor.py", task_id="depositor", dag=dag)

var_directory_of_temporary_public_art_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-temporary-public-art/transform.py", task_id="transform", dag=dag)

var_dof_cooperative_comparable_rental_income_manhattan_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-manhattan-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_2010_census_tracts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-census-tracts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_total_occupied_housing_units_by_household_size_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/total-occupied-housing-units-by-household-size-by-borough/depositor.py", task_id="depositor", dag=dag)

var_2009_10_class_size_school_level_detail_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2009-10-class-size-school-level-detail/depositor.py", task_id="depositor", dag=dag)

var_directory_of_eateries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-eateries/depositor.py", task_id="depositor", dag=dag)

var_directory_of_eateries_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-eateries/transform.py", task_id="transform", dag=dag)

var_after_school_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/after-school-programs/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_housing_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-housing/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_in_queens_for_class_1_2_and_3_family_homes_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2007/depositor.py", task_id="depositor", dag=dag)

var_recording_studios_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/recording-studios/depositor.py", task_id="depositor", dag=dag)

var_recording_studios_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/recording-studios/transform.py", task_id="transform", dag=dag)

var_family_assistance_fa_recipients_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/family-assistance-fa-recipients/depositor.py", task_id="depositor", dag=dag)

var_clean_air_survey_content_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/clean-air-survey-content-2009/depositor.py", task_id="depositor", dag=dag)

var_clean_air_survey_content_2009_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/clean-air-survey-content-2009/transform.py", task_id="transform", dag=dag)

var_fy14_mmr_data_extract_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy14-mmr-data-extract/depositor.py", task_id="depositor", dag=dag)

var_public_use_microdata_areas_puma_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/public-use-microdata-areas-puma/depositor.py", task_id="depositor", dag=dag)

var_fy17_pmmr_agency_resources_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy17-pmmr-agency-resources/depositor.py", task_id="depositor", dag=dag)

var_fulton_street_mall_businesses_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fulton-street-mall-businesses/depositor.py", task_id="depositor", dag=dag)

var_ccrb_disciplinary_recommendations_for_officers_against_whom_the_ccrb_substantiated_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-disciplinary-recommendations-for-officers-against-whom-the-ccrb-substantiated-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_inspections_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inspections/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_debt_service_since_fy_2000_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-debt-service-since-fy-2000/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_district_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-district-all-students/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_brooklyn_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-brooklyn-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_performance_directory_2014_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-performance-directory-2014-2015/depositor.py", task_id="depositor", dag=dag)

var_exemption_classification_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/exemption-classification-codes/depositor.py", task_id="depositor", dag=dag)

var_fcrc_annual_concession_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fcrc-annual-concession-plan/depositor.py", task_id="depositor", dag=dag)

var_weights_measures_and_other_tests_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/weights-measures-and-other-tests/depositor.py", task_id="depositor", dag=dag)

var_special_waste_drop_off_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/special-waste-drop-off-sites/depositor.py", task_id="depositor", dag=dag)

var_bicycle_counts_for_east_river_bridges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bicycle-counts-for-east-river-bridges/depositor.py", task_id="depositor", dag=dag)

var_bicycle_counts_for_east_river_bridges_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bicycle-counts-for-east-river-bridges/transform.py", task_id="transform", dag=dag)

var_enrollment_capacity_and_utilization_reports_district_1_32_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-district-1-32/depositor.py", task_id="depositor", dag=dag)

var_directory_of_tennis_permit_fees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-tennis-permit-fees/depositor.py", task_id="depositor", dag=dag)

var_ceqr_project_milestones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ceqr-project-milestones/depositor.py", task_id="depositor", dag=dag)

var_ccrb_average_days_for_the_ccrb_to_close_cases_measured_from_date_of_report_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-average-days-for-the-ccrb-to-close-cases-measured-from-date-of-report-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_street_hail_livery_shl_drivers_status_change_log_09182014_present_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-hail-livery-shl-drivers-status-change-log-09182014-present/depositor.py", task_id="depositor", dag=dag)

var_housing_litigations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/housing-litigations/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_in_brooklyn_for_class_1_2_and_3_family_homes_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-brooklyn-for-class-1-2-and-3-family-homes-2008/depositor.py", task_id="depositor", dag=dag)

var_areas_of_interest_gis_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/areas-of-interest-gis/depositor.py", task_id="depositor", dag=dag)

var_family_planning_benefit_program_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/family-planning-benefit-program-income-levels/depositor.py", task_id="depositor", dag=dag)

var_greenstreets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/greenstreets/depositor.py", task_id="depositor", dag=dag)

var_greenstreets_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/greenstreets/transform.py", task_id="transform", dag=dag)

var_math_test_results_2006_2012_school_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-school-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_directory_of_ice_skating_rinks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-ice-skating-rinks/depositor.py", task_id="depositor", dag=dag)

var_directory_of_ice_skating_rinks_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-ice-skating-rinks/transform.py", task_id="transform", dag=dag)

var_land_acquisition_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/land-acquisition-statistics/depositor.py", task_id="depositor", dag=dag)

var_land_acquisition_statistics_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/land-acquisition-statistics/transform.py", task_id="transform", dag=dag)

var_certificate_of_fitness_schedule_of_fees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/certificate-of-fitness-schedule-of-fees/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nature_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nature-centers/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nature_centers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nature-centers/transform.py", task_id="transform", dag=dag)

var_wtc_disorders_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wtc-disorders/depositor.py", task_id="depositor", dag=dag)

var_film_permits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/film-permits/depositor.py", task_id="depositor", dag=dag)

var_list_of_total_cases_filed_at_oath_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/list-of-total-cases-filed-at-oath/depositor.py", task_id="depositor", dag=dag)

var_borough_boundaries_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/borough-boundaries-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_2001_campaign_contributions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2001-campaign-contributions/depositor.py", task_id="depositor", dag=dag)

var_subway_entrances_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/subway-entrances/depositor.py", task_id="depositor", dag=dag)

var_annual_procurement_indicator_report_fy15_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annual-procurement-indicator-report-fy15/depositor.py", task_id="depositor", dag=dag)

var_annual_procurement_indicator_report_fy15_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annual-procurement-indicator-report-fy15/transform.py", task_id="transform", dag=dag)

var_active_projects_public_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/active-projects-public-buildings/depositor.py", task_id="depositor", dag=dag)

var_school_progress_reports_all_schools_2008_09_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-reports-all-schools-2008-09/depositor.py", task_id="depositor", dag=dag)

var_scorecard_ratings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/scorecard-ratings/depositor.py", task_id="depositor", dag=dag)

var_drinking_water_quality_distribution_monitoring_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/drinking-water-quality-distribution-monitoring-data/depositor.py", task_id="depositor", dag=dag)

var_watershed_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/watershed-statistics/depositor.py", task_id="depositor", dag=dag)

var_child_health_plus_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/child-health-plus-income-levels/depositor.py", task_id="depositor", dag=dag)

var_miscellaneous_structures_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/miscellaneous-structures/depositor.py", task_id="depositor", dag=dag)

var_lost_property_contact_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lost-property-contact-information/depositor.py", task_id="depositor", dag=dag)

var_nyc_parks_monuments_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-parks-monuments/depositor.py", task_id="depositor", dag=dag)

var_paratransit_services_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-services-bases/depositor.py", task_id="depositor", dag=dag)

var_paratransit_services_bases_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/paratransit-services-bases/transform.py", task_id="transform", dag=dag)

var_school_district_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-district-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_heating_oil_consumption_and_cost_2010_november_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/heating-oil-consumption-and-cost-2010-november-2016/depositor.py", task_id="depositor", dag=dag)

var_monthly_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/monthly-indicators/depositor.py", task_id="depositor", dag=dag)

var_unaffiliated_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/unaffiliated-vehicles/depositor.py", task_id="depositor", dag=dag)

var_unaffiliated_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/unaffiliated-vehicles/transform.py", task_id="transform", dag=dag)

var_intake_within_and_outside_ccrb_jurisdiction_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/intake-within-and-outside-ccrb-jurisdiction/depositor.py", task_id="depositor", dag=dag)

var_council_district_breakdown_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/council-district-breakdown/depositor.py", task_id="depositor", dag=dag)

var_black_car_services_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/black-car-services-vehicles/depositor.py", task_id="depositor", dag=dag)

var_black_car_services_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/black-car-services-vehicles/transform.py", task_id="transform", dag=dag)

var_entry_point_lcr_monitoring_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/entry-point-lcr-monitoring-results/depositor.py", task_id="depositor", dag=dag)

var_cable_franchise_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cable-franchise-areas/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_for_manhattan_for_class_1_2_and_3_family_homes_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-for-manhattan-for-class-1-2-and-3-family-homes-2009/depositor.py", task_id="depositor", dag=dag)

var_enrollment_capacity_and_utilization_reports_target_by_organization_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-target-by-organization/depositor.py", task_id="depositor", dag=dag)

var_directory_of_beaches_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-beaches/depositor.py", task_id="depositor", dag=dag)

var_directory_of_beaches_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-beaches/transform.py", task_id="transform", dag=dag)

var_new_york_state_english_language_arts_ela_exam_by_school_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-state-english-language-arts-ela-exam-by-school/depositor.py", task_id="depositor", dag=dag)

var_directory_of_zoos_and_aquariums_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-zoos-and-aquariums/depositor.py", task_id="depositor", dag=dag)

var_directory_of_zoos_and_aquariums_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-zoos-and-aquariums/transform.py", task_id="transform", dag=dag)

var_open_parking_and_camera_violations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-parking-and-camera-violations/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_district_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-district-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_street_weekly_resurfacing_schedule_queens_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-weekly-resurfacing-schedule-queens/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_citywide_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-citywide-gender/depositor.py", task_id="depositor", dag=dag)

var_directory_of_unsheltered_street_homeless_to_general_population_ratio_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-unsheltered-street-homeless-to-general-population-ratio-2011/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_school_level_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-school-level-all-students/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_special_operations_division_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-special-operations-division-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_hpd_fund_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-fund-element/depositor.py", task_id="depositor", dag=dag)

var_directory_of_programs_list_mayors_office_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-programs-list-mayors-office/depositor.py", task_id="depositor", dag=dag)

var_acceptable_reduced_pressure_zone_devices_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acceptable-reduced-pressure-zone-devices/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_work_and_family_leave_survey_wfls_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-work-and-family-leave-survey-wfls-2014/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_brooklyn_south_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-brooklyn-south-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_district_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-district-all-students/depositor.py", task_id="depositor", dag=dag)

var_government_issued_personal_identification_for_youth_in_foster_care_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/government-issued-personal-identification-for-youth-in-foster-care/depositor.py", task_id="depositor", dag=dag)

var_government_issued_personal_identification_for_youth_in_foster_care_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/government-issued-personal-identification-for-youth-in-foster-care/transform.py", task_id="transform", dag=dag)

var_new_york_city_population_by_community_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-population-by-community-districts/depositor.py", task_id="depositor", dag=dag)

var_transit_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/transit-zones/depositor.py", task_id="depositor", dag=dag)

var_dohmh_new_york_city_restaurant_inspection_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dohmh-new-york-city-restaurant-inspection-results/depositor.py", task_id="depositor", dag=dag)

var_cost_summary_by_citywide_category_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cost-summary-by-citywide-category/depositor.py", task_id="depositor", dag=dag)

var_nycha_psa_police_service_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-psa-police-service-areas/depositor.py", task_id="depositor", dag=dag)

var_forestry_work_orders_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/forestry-work-orders/depositor.py", task_id="depositor", dag=dag)

var_subway_lines_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/subway-lines/depositor.py", task_id="depositor", dag=dag)

var_energy_and_water_data_disclosure_for_local_law_84_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-and-water-data-disclosure-for-local-law-84-2013/depositor.py", task_id="depositor", dag=dag)

var_2010_2011_class_size_school_level_detail_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-2011-class-size-school-level-detail/depositor.py", task_id="depositor", dag=dag)

var_directory_of_business_improvement_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-business-improvement-districts/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_bronx_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-bronx-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nycha_community_facilities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nycha-community-facilities/depositor.py", task_id="depositor", dag=dag)

var_distribution_of_discourtesy_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/distribution-of-discourtesy-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_homeless_population_by_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-homeless-population-by-year/depositor.py", task_id="depositor", dag=dag)

var_2006_07_class_size_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2006-07-class-size-by-borough/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_traffic_control_division_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-traffic-control-division-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_all_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-all-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_new_york_city_police_pension_fund_financial_reports_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-new-york-city-police-pension-fund-financial-reports/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_investigations_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-investigations-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_self_hauler_registrants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/self-hauler-registrants/depositor.py", task_id="depositor", dag=dag)

var_directory_of_bocce_courts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-bocce-courts/depositor.py", task_id="depositor", dag=dag)

var_directory_of_bocce_courts_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-bocce-courts/transform.py", task_id="transform", dag=dag)

var_water_resevoir_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/water-resevoir-levels/depositor.py", task_id="depositor", dag=dag)

var_handyman_work_order_hwo_charges_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/handyman-work-order-hwo-charges/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_citywide_for_class_1_2_and_3_family_homes_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-citywide-for-class-1-2-and-3-family-homes-2008/depositor.py", task_id="depositor", dag=dag)

var_bus_breakdown_and_delays_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bus-breakdown-and-delays/depositor.py", task_id="depositor", dag=dag)

var_nyc_open_data_plan_scheduled_releases_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-open-data-plan-scheduled-releases-2016/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_citywide_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-citywide-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_manhattan_south_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-manhattan-south-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_worst_case_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-worst-case/depositor.py", task_id="depositor", dag=dag)

var_60_month_converted_to_safety_net_sn_recipients_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/60-month-converted-to-safety-net-sn-recipients/depositor.py", task_id="depositor", dag=dag)

var_2013_2014_school_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2013-2014-school-zones/depositor.py", task_id="depositor", dag=dag)

var_open_space_other_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-space-other/depositor.py", task_id="depositor", dag=dag)

var_library_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/library/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_brooklyn_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-brooklyn-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_map_of_soccer_and_football_fields_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/map-of-soccer-and-football-fields/depositor.py", task_id="depositor", dag=dag)

var_hpd_tax_incentive_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-tax-incentive-element/depositor.py", task_id="depositor", dag=dag)

var_wic_income_eligibility_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wic-income-eligibility/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_transit_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-transit-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2010/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2010_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2010/transform.py", task_id="transform", dag=dag)

var_inmate_deaths_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-deaths/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_farmers_markets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-farmers-markets/depositor.py", task_id="depositor", dag=dag)

var_community_car_services_livery_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-car-services-livery-vehicles/depositor.py", task_id="depositor", dag=dag)

var_community_car_services_livery_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-car-services-livery-vehicles/transform.py", task_id="transform", dag=dag)

var_dcla_cultural_organizations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-cultural-organizations/depositor.py", task_id="depositor", dag=dag)

var_nyc_open_data_removed_datasets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-open-data-removed-datasets/depositor.py", task_id="depositor", dag=dag)

var_nycdcp_manhattan_bike_counts_on_street_weekday_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycdcp-manhattan-bike-counts-on-street-weekday/depositor.py", task_id="depositor", dag=dag)

var_directory_of_new_york_city_police_pension_fund_contact_numbers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-new-york-city-police-pension-fund-contact-numbers/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_in_the_bronx_for_class_1_2_and_3_family_homes_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-the-bronx-for-class-1-2-and-3-family-homes-2008/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_classes_of_2005_2010_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-classes-of-2005-2010-by-borough/depositor.py", task_id="depositor", dag=dag)

var_open_summonses_active_for_hire_vehicle_fhv_owners_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-summonses-active-for-hire-vehicle-fhv-owners/depositor.py", task_id="depositor", dag=dag)

var_open_summonses_active_for_hire_vehicle_fhv_owners_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-summonses-active-for-hire-vehicle-fhv-owners/transform.py", task_id="transform", dag=dag)

var_graduation_outcomes_school_level_classes_of_2005_2011_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-of-2005-2011-gender/depositor.py", task_id="depositor", dag=dag)

var_alliance_for_downtown_new_york_big_apps_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/alliance-for-downtown-new-york-big-apps-data/depositor.py", task_id="depositor", dag=dag)

var_alliance_for_downtown_new_york_big_apps_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/alliance-for-downtown-new-york-big-apps-data/transform.py", task_id="transform", dag=dag)

var_tax_credits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tax-credits/depositor.py", task_id="depositor", dag=dag)

var_grand_street_bid_business_directory_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/grand-street-bid-business-directory/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_out_of_school_time_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-out-of-school-time/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_agency_expenditures_fy_1980_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-agency-expenditures-fy-1980-2013/depositor.py", task_id="depositor", dag=dag)

var_nycdcp_manhattan_bike_counts_off_street_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycdcp-manhattan-bike-counts-off-street/depositor.py", task_id="depositor", dag=dag)

var_citywide_hra_administered_medicaid_enrollees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citywide-hra-administered-medicaid-enrollees/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_manhattan_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-manhattan-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_nda_adult_literacy_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-nda-adult-literacy-programs/depositor.py", task_id="depositor", dag=dag)

var_art_in_doe_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/art-in-doe-buildings/depositor.py", task_id="depositor", dag=dag)

var_scout_conditions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/scout-conditions/depositor.py", task_id="depositor", dag=dag)

var_demographic_projection_report_enrollment_projections_new_york_city_public_schools_prepared_by_statistical_forecasting_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-statistical-forecasting/depositor.py", task_id="depositor", dag=dag)

var_procurement_by_industry_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/procurement-by-industry/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_supervision_passthrough_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-supervision-passthrough-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_functional_parkland_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/functional-parkland/depositor.py", task_id="depositor", dag=dag)

var_landcover_raster_data_2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/landcover-raster-data-2010/depositor.py", task_id="depositor", dag=dag)

var_landcover_raster_data_2010_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/landcover-raster-data-2010/transform.py", task_id="transform", dag=dag)

var_community_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_quality_of_life_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/quality-of-life-indicators/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_offensive_language_allegations_2005_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-offensive-language-allegations-2005/depositor.py", task_id="depositor", dag=dag)

var_population_change_for_20_largest_cities_in_the_united_states_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/population-change-for-20-largest-cities-in-the-united-states/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_population_by_neighborhood_tabulation_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-population-by-neighborhood-tabulation-areas/depositor.py", task_id="depositor", dag=dag)

var_nyc_service_volunteer_opportunities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-service-volunteer-opportunities/depositor.py", task_id="depositor", dag=dag)

var_dcla_programs_funding_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-programs-funding/depositor.py", task_id="depositor", dag=dag)

var_brooklyn_public_library_catalog_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/brooklyn-public-library-catalog/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_offensive_language_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-offensive-language-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_tlc_commuter_van_authorizations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tlc-commuter-van-authorizations/depositor.py", task_id="depositor", dag=dag)

var_directory_of_homebase_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-homebase-locations/depositor.py", task_id="depositor", dag=dag)

var_air_quality_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/air-quality/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_health_and_hospitals_corporation_hhc_hhc_options_common_fees_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-health-and-hospitals-corporation-hhc-hhc-options-common-fees/depositor.py", task_id="depositor", dag=dag)

var_times_square_hotels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-hotels/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_capital_expenditures_since_1985_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-capital-expenditures-since-1985/depositor.py", task_id="depositor", dag=dag)

var_hi_caps_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hi-caps/depositor.py", task_id="depositor", dag=dag)

var_tlc_luxury_limousine_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tlc-luxury-limousine-bases/depositor.py", task_id="depositor", dag=dag)

var_new_capacity_program_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-capacity-program-by-borough/depositor.py", task_id="depositor", dag=dag)

var_grier_partnership_part_c_demographic_projection_report_enrollment_projections_new_york_city_public_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/grier-partnership-part-c-demographic-projection-report-enrollment-projections-new-york-city-public-schools/depositor.py", task_id="depositor", dag=dag)

var_hpd_rent_affordability_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-rent-affordability-element/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_school_level_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-school-level-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_wirednyc_participating_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wirednyc-participating-buildings/depositor.py", task_id="depositor", dag=dag)

var_taxi_improvement_fund_tif_medallion_payments_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/taxi-improvement-fund-tif-medallion-payments/depositor.py", task_id="depositor", dag=dag)

var_detention_and_placement_demographic_reports_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/detention-and-placement-demographic-reports/depositor.py", task_id="depositor", dag=dag)

var_detention_and_placement_demographic_reports_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/detention-and-placement-demographic-reports/transform.py", task_id="transform", dag=dag)

var_new_york_city_health_and_hospitals_corporation_hhc_patient_satisfaction_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-health-and-hospitals-corporation-hhc-patient-satisfaction-2009/depositor.py", task_id="depositor", dag=dag)

var_lot_cleaning_dispositions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/lot-cleaning-dispositions/depositor.py", task_id="depositor", dag=dag)

var_type_number_of_allegation_complaints_received_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/type-number-of-allegation-complaints-received/depositor.py", task_id="depositor", dag=dag)

var_2012_nyc_farmers_market_list_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2012-nyc-farmers-market-list/depositor.py", task_id="depositor", dag=dag)

var_nyc_street_centerline_cscl_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-street-centerline-cscl/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_queens_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-queens-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_damage_by_sandy_by_land_use_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/damage-by-sandy-by-land-use/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_discourtesy_allegations_2006_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-discourtesy-allegations-2006/depositor.py", task_id="depositor", dag=dag)

var_audited_register_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/audited-register-data/depositor.py", task_id="depositor", dag=dag)

var_cash_assistance_recipients_since_1955_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cash-assistance-recipients-since-1955/depositor.py", task_id="depositor", dag=dag)

var_sandy_inundation_zone_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sandy-inundation-zone/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_class_of_2010_regents_based_math_ela_apm_school_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-class-of-2010-regents-based-math-ela-apm-school-level/depositor.py", task_id="depositor", dag=dag)

var_types_of_allegations_in_complaints_received_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/types-of-allegations-in-complaints-received-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_address_points_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-address-points/depositor.py", task_id="depositor", dag=dag)

var_queens_library_branches_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/queens-library-branches/depositor.py", task_id="depositor", dag=dag)

var_revenue_budget_financial_plan_qtr1_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/revenue-budget-financial-plan-qtr1/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_population_by_boroughs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-population-by-boroughs/depositor.py", task_id="depositor", dag=dag)

var_map_of_nycha_community_engagement_partnership_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/map-of-nycha-community-engagement-partnership-zones/depositor.py", task_id="depositor", dag=dag)

var_litter_basket_inventory_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/litter-basket-inventory/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_classes_of_2005_2010_school_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-classes-of-2005-2010-school-level/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_museums_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-museums/depositor.py", task_id="depositor", dag=dag)

var_2006_07_class_size_by_district_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2006-07-class-size-by-district/depositor.py", task_id="depositor", dag=dag)

var_forestry_planting_spaces_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/forestry-planting-spaces/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_bronx_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-bronx/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_bronx_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-bronx/transform.py", task_id="transform", dag=dag)

var_detention_and_placement_abuseneglect_reports_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/detention-and-placement-abuseneglect-reports/depositor.py", task_id="depositor", dag=dag)

var_detention_and_placement_abuseneglect_reports_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/detention-and-placement-abuseneglect-reports/transform.py", task_id="transform", dag=dag)

var_directory_of_hospitals_with_domestic_violence_coordinators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-hospitals-with-domestic-violence-coordinators/depositor.py", task_id="depositor", dag=dag)

var_times_square_pedestrian_counts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-pedestrian-counts/depositor.py", task_id="depositor", dag=dag)

var_times_square_pedestrian_counts_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-pedestrian-counts/transform.py", task_id="transform", dag=dag)

var_dop_juvenile_case_count_by_type_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-case-count-by-type/depositor.py", task_id="depositor", dag=dag)

var_average_salaries_in_department_of_correction_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/average-salaries-in-department-of-correction/depositor.py", task_id="depositor", dag=dag)

var_permit_application_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/permit-application-information/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_school_level_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-school-level-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_current_commuter_van_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/current-commuter-van-drivers/depositor.py", task_id="depositor", dag=dag)

var_pmmr_2014_raw_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/pmmr-2014-raw-data/depositor.py", task_id="depositor", dag=dag)

var_school_progress_report_multi_year_2007_2011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-report-multi-year-2007-2011/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_traffic_control_division_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-traffic-control-division-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_in_manhattan_for_class_1_2_and_3_family_homes_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-manhattan-for-class-1-2-and-3-family-homes-2008/depositor.py", task_id="depositor", dag=dag)

var_for_hire_vehicles_fhv_active_and_inactive_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/for-hire-vehicles-fhv-active-and-inactive-vehicles/depositor.py", task_id="depositor", dag=dag)

var_primary_commercial_zoning_by_lot_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/primary-commercial-zoning-by-lot/depositor.py", task_id="depositor", dag=dag)

var_oil_boilers_detailed_fuel_consumption_and_building_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/oil-boilers-detailed-fuel-consumption-and-building-data/depositor.py", task_id="depositor", dag=dag)

var_census_demographics_at_the_nyc_community_district_cd_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/census-demographics-at-the-nyc-community-district-cd-level/depositor.py", task_id="depositor", dag=dag)

var_census_demographics_at_the_nyc_community_district_cd_level_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/census-demographics-at-the-nyc-community-district-cd-level/transform.py", task_id="transform", dag=dag)

var_math_test_results_2006_2012_borough_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-borough-gender/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_bronx_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-bronx-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_parks_inspections_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parks-inspections-data/depositor.py", task_id="depositor", dag=dag)

var_parks_inspections_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parks-inspections-data/transform.py", task_id="transform", dag=dag)

var_dof_cooperative_comparable_rental_income_bronx_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-bronx-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_ccrb_disposition_of_abuse_of_authority_allegations_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-disposition-of-abuse-of-authority-allegations-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_sca_disqualified_firms_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sca-disqualified-firms/depositor.py", task_id="depositor", dag=dag)

var_fy2013_mmr_data_extract_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy2013-mmr-data-extract/depositor.py", task_id="depositor", dag=dag)

var_acris_country_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acris-country-codes/depositor.py", task_id="depositor", dag=dag)

var_parking_lots_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-lots/depositor.py", task_id="depositor", dag=dag)

var_derelict_vehicle_dispositions_tow_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/derelict-vehicle-dispositions-tow/depositor.py", task_id="depositor", dag=dag)

var_citizen_emergency_response_team_cert_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citizen-emergency-response-team-cert/depositor.py", task_id="depositor", dag=dag)

var_hpd_project_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-project-element/depositor.py", task_id="depositor", dag=dag)

var_acceptable_reduced_pressure_detector_assemblies_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acceptable-reduced-pressure-detector-assemblies/depositor.py", task_id="depositor", dag=dag)

var_fair_student_funding_budget_detail_1_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fair-student-funding-budget-detail-1/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_violations_of_probation_filed_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-violations-of-probation-filed-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_rate_at_which_the_ccrb_made_findings_on_the_merits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/rate-at-which-the-ccrb-made-findings-on-the-merits/depositor.py", task_id="depositor", dag=dag)

var_directory_of_homeless_drop_in_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-homeless-drop-in-centers/depositor.py", task_id="depositor", dag=dag)

var_miny_vendors_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/miny-vendors/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_queens_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-queens-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_district_by_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-district-by-gender/depositor.py", task_id="depositor", dag=dag)

var_theaters_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/theaters/depositor.py", task_id="depositor", dag=dag)

var_dohmh_beach_water_quality_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dohmh-beach-water-quality-data/depositor.py", task_id="depositor", dag=dag)

var_ap_college_board_2010_school_level_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ap-college-board-2010-school-level-results/depositor.py", task_id="depositor", dag=dag)

var_dcla_cultural_organization_resources_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dcla-cultural-organization-resources/depositor.py", task_id="depositor", dag=dag)

var_fire_divisions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fire-divisions/depositor.py", task_id="depositor", dag=dag)

var_workforce1_recruitment_events_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/workforce1-recruitment-events/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_queens_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-queens-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_cultural_institutions_by_block_and_lot_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cultural-institutions-by-block-and-lot/depositor.py", task_id="depositor", dag=dag)

var_revenue_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/revenue/depositor.py", task_id="depositor", dag=dag)

var_oem_emergency_notifications_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/oem-emergency-notifications/depositor.py", task_id="depositor", dag=dag)

var_tlc_driver_education_24_hour_course_providers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tlc-driver-education-24-hour-course-providers/depositor.py", task_id="depositor", dag=dag)

var_dop_eligible_diversion_rate_for_juveniles_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-eligible-diversion-rate-for-juveniles-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_street_weekly_resurfacing_schedule_brooklyn_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-weekly-resurfacing-schedule-brooklyn/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_discourtesy_allegations_2008_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-discourtesy-allegations-2008-2/depositor.py", task_id="depositor", dag=dag)

var_active_uniform_staff_by_rank_and_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/active-uniform-staff-by-rank-and-gender/depositor.py", task_id="depositor", dag=dag)

var_directory_of_historic_houses_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-historic-houses/depositor.py", task_id="depositor", dag=dag)

var_directory_of_historic_houses_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-historic-houses/transform.py", task_id="transform", dag=dag)

var_2010_2011_class_size_citywide_distribution_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-2011-class-size-citywide-distribution/depositor.py", task_id="depositor", dag=dag)

var_law_press_releases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/law-press-releases/depositor.py", task_id="depositor", dag=dag)

var_property_valuation_and_assessment_data_tax_class_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-valuation-and-assessment-data-tax-class/depositor.py", task_id="depositor", dag=dag)

var_property_valuation_and_assessment_data_tax_class_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-valuation-and-assessment-data-tax-class/transform.py", task_id="transform", dag=dag)

var_nyc_zoning_tax_lot_database_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-zoning-tax-lot-database/depositor.py", task_id="depositor", dag=dag)

var_hra_domestic_violence_partners_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hra-domestic-violence-partners/depositor.py", task_id="depositor", dag=dag)

var_directory_of_unsheltered_street_homeless_to_general_population_ratio_2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-unsheltered-street-homeless-to-general-population-ratio-2010/depositor.py", task_id="depositor", dag=dag)

var_hydrostats_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hydrostats/depositor.py", task_id="depositor", dag=dag)

var_shl_meter_shops_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/shl-meter-shops/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_revenue_and_spending_summary_fy_1980_fy_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-revenue-and-spending-summary-fy-1980-fy-2013/depositor.py", task_id="depositor", dag=dag)

var_acris_ucc_collateral_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/acris-ucc-collateral-codes/depositor.py", task_id="depositor", dag=dag)

var_capital_commitments_all_funds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capital-commitments-all-funds/depositor.py", task_id="depositor", dag=dag)

var_fdny_monthly_response_times_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-monthly-response-times/depositor.py", task_id="depositor", dag=dag)

var_heating_gas_consumption_and_cost_2010_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/heating-gas-consumption-and-cost-2010-2016/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_n_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-n/depositor.py", task_id="depositor", dag=dag)

var_swimming_pools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/swimming-pools/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_nnw_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-nnw/depositor.py", task_id="depositor", dag=dag)

var_quality_review_2005_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/quality-review-2005-2012/depositor.py", task_id="depositor", dag=dag)

var_pavement_edge_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/pavement-edge/depositor.py", task_id="depositor", dag=dag)

var_fc_bid_walkof_fame_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fc-bid-walkof-fame-data/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_case_closings_by_reason_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-case-closings-by-reason/depositor.py", task_id="depositor", dag=dag)

var_directory_of_recreation_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-recreation-centers/depositor.py", task_id="depositor", dag=dag)

var_directory_of_recreation_centers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-recreation-centers/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_school_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-school-swd/depositor.py", task_id="depositor", dag=dag)

var_downtown_brooklyn_partnership_dbp_court_livingston_schermerhorn_cls_retail_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/downtown-brooklyn-partnership-dbp-court-livingston-schermerhorn-cls-retail-locations/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_of_2005_2011_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-of-2005-2011-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_annualized_rolling_sales_update_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annualized-rolling-sales-update/depositor.py", task_id="depositor", dag=dag)

var_annualized_rolling_sales_update_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annualized-rolling-sales-update/transform.py", task_id="transform", dag=dag)

var_health_and_hospitals_corporation_hhc_facilities_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/health-and-hospitals-corporation-hhc-facilities/depositor.py", task_id="depositor", dag=dag)

var_law_published_columns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/law-published-columns/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_force_allegations_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-force-allegations-2008/depositor.py", task_id="depositor", dag=dag)

var_enrollment_capacity_and_utilization_reports_target_by_building_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-target-by-building/depositor.py", task_id="depositor", dag=dag)

var_parking_lot_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-lot/depositor.py", task_id="depositor", dag=dag)

var_forestry_inspections_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/forestry-inspections/depositor.py", task_id="depositor", dag=dag)

var_anticipated_rfp_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/anticipated-rfp/depositor.py", task_id="depositor", dag=dag)

var_fy16_pmmr_agency_resources_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy16-pmmr-agency-resources/depositor.py", task_id="depositor", dag=dag)

var_nyc_municipal_building_energy_benchmarking_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-municipal-building-energy-benchmarking-results/depositor.py", task_id="depositor", dag=dag)

var_group_ride_vehicle_pilot_program_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/group-ride-vehicle-pilot-program-bases/depositor.py", task_id="depositor", dag=dag)

var_group_ride_vehicle_pilot_program_bases_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/group-ride-vehicle-pilot-program-bases/transform.py", task_id="transform", dag=dag)

var_city_bench_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-bench-locations/depositor.py", task_id="depositor", dag=dag)

var_city_bench_locations_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-bench-locations/transform.py", task_id="transform", dag=dag)

var_2014_nyc_open_data_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-nyc-open-data-plan/depositor.py", task_id="depositor", dag=dag)

var_firearms_discharge_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/firearms-discharge-report/depositor.py", task_id="depositor", dag=dag)

var_dop_eligible_diversion_rate_for_juveniles_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-eligible-diversion-rate-for-juveniles-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_hurricane_evacuation_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-evacuation-zones/depositor.py", task_id="depositor", dag=dag)

var_incidents_responded_to_by_fire_companies_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/incidents-responded-to-by-fire-companies/depositor.py", task_id="depositor", dag=dag)

var_property_tax_rates_by_tax_class_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-tax-rates-by-tax-class/depositor.py", task_id="depositor", dag=dag)

var_nyc_open_data_plan_datasets_added_since_the_publication_nyc_open_data_plan_september_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-open-data-plan-datasets-added-since-the-publication-nyc-open-data-plan-september-2013/depositor.py", task_id="depositor", dag=dag)

var_nyc_business_acceleration_businesses_served_and_jobs_created_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-business-acceleration-businesses-served-and-jobs-created/depositor.py", task_id="depositor", dag=dag)

var_plazas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/plazas/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_abuse_of_authority_allegations_2005_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-abuse-of-authority-allegations-2005/depositor.py", task_id="depositor", dag=dag)

var_waterfront_access_plans_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/waterfront-access-plans/depositor.py", task_id="depositor", dag=dag)

var_update_to_submitted_state_aid_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/update-to-submitted-state-aid-projects/depositor.py", task_id="depositor", dag=dag)

var_fcrc_annual_concession_plan_franchises_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fcrc-annual-concession-plan-franchises/depositor.py", task_id="depositor", dag=dag)

var_council_members_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/council-members/depositor.py", task_id="depositor", dag=dag)

var_roadbed_pointer_list_rpl_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/roadbed-pointer-list-rpl/depositor.py", task_id="depositor", dag=dag)

var_roadbed_pointer_list_rpl_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/roadbed-pointer-list-rpl/transform.py", task_id="transform", dag=dag)

var_projected_median_age_by_borough_2000_2030_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-median-age-by-borough-2000-2030/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_district_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-district-ell/depositor.py", task_id="depositor", dag=dag)

var_luxury_limousine_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/luxury-limousine-vehicles/depositor.py", task_id="depositor", dag=dag)

var_nycdep_recreation_area_maps_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycdep-recreation-area-maps/depositor.py", task_id="depositor", dag=dag)

var_police_precincts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/police-precincts/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_of_2005_2011_ell_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-of-2005-2011-ell/depositor.py", task_id="depositor", dag=dag)

var_sidewalk_weekly_construction_schedule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk-weekly-construction-schedule/depositor.py", task_id="depositor", dag=dag)

var_2009_campaign_expenditures_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2009-campaign-expenditures/depositor.py", task_id="depositor", dag=dag)

var_railroad_structure_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/railroad-structure/depositor.py", task_id="depositor", dag=dag)

var_play_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/play-areas/depositor.py", task_id="depositor", dag=dag)

var_2003_campaign_contributions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2003-campaign-contributions/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_adolescent_literacy_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-adolescent-literacy/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_brooklyn_south_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-brooklyn-south-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_staten_island_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-staten-island-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_ccrb_age_of_substantiated_cases_measured_from_the_date_of_report_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-age-of-substantiated-cases-measured-from-the-date-of-report-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_district_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-district-swd/depositor.py", task_id="depositor", dag=dag)

var_applications_tracking_table_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/applications-tracking-table/depositor.py", task_id="depositor", dag=dag)

var_idnyc_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/idnyc-locations/depositor.py", task_id="depositor", dag=dag)

var_mandatory_inclusionary_housing_mih_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/mandatory-inclusionary-housing-mih/depositor.py", task_id="depositor", dag=dag)

var_community_car_services_livery_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-car-services-livery-bases/depositor.py", task_id="depositor", dag=dag)

var_community_car_services_livery_bases_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-car-services-livery-bases/transform.py", task_id="transform", dag=dag)

var_city_tax_revenue_financial_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/city-tax-revenue-financial-plan/depositor.py", task_id="depositor", dag=dag)

var_ipis_integrated_property_information_system_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ipis-integrated-property-information-system/depositor.py", task_id="depositor", dag=dag)

var_youth_behavior_risk_survey_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/youth-behavior-risk-survey/depositor.py", task_id="depositor", dag=dag)

var_energy_and_water_data_disclosure_for_local_law_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-and-water-data-disclosure-for-local-law-2014/depositor.py", task_id="depositor", dag=dag)

var_enrollment_capacity_and_utilization_reports_district_75_special_ed_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-district-75-special-ed/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_bronx_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-bronx-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_drought_regulation_penalty_schedule_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/drought-regulation-penalty-schedule/depositor.py", task_id="depositor", dag=dag)

var_local_law_1_city_council_report_fy_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-1-city-council-report-fy-2015/depositor.py", task_id="depositor", dag=dag)

var_local_law_1_city_council_report_fy_2015_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-1-city-council-report-fy-2015/transform.py", task_id="transform", dag=dag)

var_natural_gas_consumption_by_zip_code_2010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/natural-gas-consumption-by-zip-code-2010/depositor.py", task_id="depositor", dag=dag)

var_assignment_of_officers_against_whom_allegations_were_substantiated_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/assignment-of-officers-against-whom-allegations-were-substantiated/depositor.py", task_id="depositor", dag=dag)

var_community_board_appointments_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-board-appointments/depositor.py", task_id="depositor", dag=dag)

var_directory_of_senior_news_services_in_nycha_journal_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-senior-news-services-in-nycha-journal/depositor.py", task_id="depositor", dag=dag)

var_target_community_district_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/target-community-district/depositor.py", task_id="depositor", dag=dag)

var_jfk_airtrain_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/jfk-airtrain/depositor.py", task_id="depositor", dag=dag)

var_2015_street_tree_census_blockface_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2015-street-tree-census-blockface-data/depositor.py", task_id="depositor", dag=dag)

var_nyc_municipal_building_energy_benchmarking_results_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-municipal-building-energy-benchmarking-results-2014/depositor.py", task_id="depositor", dag=dag)

var_where_incidents_that_led_to_a_substantiated_complaint_took_place_queens_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-substantiated-complaint-took-place-queens-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_civil_service_list_active_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/civil-service-list-active/depositor.py", task_id="depositor", dag=dag)

var_borough_boundaries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/borough-boundaries/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_school_level_by_disability_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-school-level-by-disability-status/depositor.py", task_id="depositor", dag=dag)

var_directory_of_playgrounds_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-playgrounds/depositor.py", task_id="depositor", dag=dag)

var_directory_of_playgrounds_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-playgrounds/transform.py", task_id="transform", dag=dag)

var_dycd_after_school_programs_syep_summer_youth_employment_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-syep-summer-youth-employment-programs/depositor.py", task_id="depositor", dag=dag)

var_building_footprints_historical_shape_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/building-footprints-historical-shape/depositor.py", task_id="depositor", dag=dag)

var_dof_cooperative_comparable_rental_income_staten_island_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-cooperative-comparable-rental-income-staten-island-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_expense_financial_plan_qtr1_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/expense-financial-plan-qtr1/depositor.py", task_id="depositor", dag=dag)

var_tax_liability_by_agi_range_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tax-liability-by-agi-range/depositor.py", task_id="depositor", dag=dag)

var_dycd_syep_summer_youth_employment_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-syep-summer-youth-employment/depositor.py", task_id="depositor", dag=dag)

var_street_weekly_resurfacing_schedule_manhattan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-weekly-resurfacing-schedule-manhattan/depositor.py", task_id="depositor", dag=dag)

var_2014_2015_school_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-2015-school-zones/depositor.py", task_id="depositor", dag=dag)

var_energy_efficiency_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-efficiency-projects/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_citywide_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-citywide-gender/depositor.py", task_id="depositor", dag=dag)

var_health_center_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/health-center-districts/depositor.py", task_id="depositor", dag=dag)

var_new_york_state_mathematics_exam_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-state-mathematics-exam/depositor.py", task_id="depositor", dag=dag)

var_directory_of_unsheltered_street_homeless_to_general_population_ratio_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-unsheltered-street-homeless-to-general-population-ratio-2009/depositor.py", task_id="depositor", dag=dag)

var_tlc_authorized_behind_the_wheel_providers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/tlc-authorized-behind-the-wheel-providers/depositor.py", task_id="depositor", dag=dag)

var_dycd_yaip_young_adult_internship_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-yaip-young-adult-internship-programs/depositor.py", task_id="depositor", dag=dag)

var_2005_street_tree_census_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2005-street-tree-census/depositor.py", task_id="depositor", dag=dag)

var_how_complaints_filed_with_the_nypd_were_reported_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/how-complaints-filed-with-the-nypd-were-reported-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_awarded_construction_contracts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-awarded-construction-contracts/depositor.py", task_id="depositor", dag=dag)

var_capital_commitments_exec_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capital-commitments-exec/depositor.py", task_id="depositor", dag=dag)

var_high_school_graduation_rates_of_youth_in_foster_care_annual_report_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/high-school-graduation-rates-of-youth-in-foster-care-annual-report-2015/depositor.py", task_id="depositor", dag=dag)

var_high_school_graduation_rates_of_youth_in_foster_care_annual_report_2015_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/high-school-graduation-rates-of-youth-in-foster-care-annual-report-2015/transform.py", task_id="transform", dag=dag)

var_2016_for_hire_vehicle_trip_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2016-for-hire-vehicle-trip-data/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_meals_income_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-meals-income-levels/depositor.py", task_id="depositor", dag=dag)

var_fy17_pmmr_spending_and_budget_information_by_units_of_appropriation_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy17-pmmr-spending-and-budget-information-by-units-of-appropriation/depositor.py", task_id="depositor", dag=dag)

var_sat_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sat-results/depositor.py", task_id="depositor", dag=dag)

var_directory_of_job_centers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-job-centers/depositor.py", task_id="depositor", dag=dag)

var_group_ride_vehicle_pilot_program_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/group-ride-vehicle-pilot-program-vehicles/depositor.py", task_id="depositor", dag=dag)

var_group_ride_vehicle_pilot_program_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/group-ride-vehicle-pilot-program-vehicles/transform.py", task_id="transform", dag=dag)

var_local_law_50_new_york_state_food_purchasing_fy15_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-50-new-york-state-food-purchasing-fy15/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_2010_2011_regents_based_mathela_apm_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-swd/depositor.py", task_id="depositor", dag=dag)

var_parking_violations_issued_fiscal_year_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-violations-issued-fiscal-year-2015/depositor.py", task_id="depositor", dag=dag)

var_sustainability_indicators_2012_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sustainability-indicators-2012-2/depositor.py", task_id="depositor", dag=dag)

var_sustainability_indicators_2012_2_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sustainability-indicators-2012-2/transform.py", task_id="transform", dag=dag)

var_demographic_projection_report_enrollment_projections_new_york_city_public_schools_prepared_by_the_grier_partnership_part_b_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-the-grier-partnership-part-b/depositor.py", task_id="depositor", dag=dag)

var_enrollment_capacity_and_utilization_reports_alternative_hs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/enrollment-capacity-and-utilization-reports-alternative-hs/depositor.py", task_id="depositor", dag=dag)

var_zoning_map_index_quartersection_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/zoning-map-index-quartersection/depositor.py", task_id="depositor", dag=dag)

var_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/vehicles/depositor.py", task_id="depositor", dag=dag)

var_residence_of_subject_officers_against_whom_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/residence-of-subject-officers-against-whom-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_current_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/current-bases/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_force_allegations_2006_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-force-allegations-2006/depositor.py", task_id="depositor", dag=dag)

var_dof_parking_violation_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-parking-violation-codes/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_manhattan_fy_20112012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-manhattan-fy-20112012/depositor.py", task_id="depositor", dag=dag)

var_appeals_closed_in_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/appeals-closed-in-2016/depositor.py", task_id="depositor", dag=dag)

var_curbs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/curbs/depositor.py", task_id="depositor", dag=dag)

var_medicaid_offices_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medicaid-offices/depositor.py", task_id="depositor", dag=dag)

var_approved_licensees_and_registrants_for_trade_waste_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/approved-licensees-and-registrants-for-trade-waste/depositor.py", task_id="depositor", dag=dag)

var_directory_historical_signs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-historical-signs/depositor.py", task_id="depositor", dag=dag)

var_directory_historical_signs_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-historical-signs/transform.py", task_id="transform", dag=dag)

var_senate_district_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/senate-district-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_race_of_victims_with_substantiated_allegations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/race-of-victims-with-substantiated-allegations/depositor.py", task_id="depositor", dag=dag)

var_law_public_service_program_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/law-public-service-program/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_citywide_for_class_1_2_and_3_family_homes_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-citywide-for-class-1-2-and-3-family-homes-2009/depositor.py", task_id="depositor", dag=dag)

var_environmentally_preferable_procurements_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/environmentally-preferable-procurements/depositor.py", task_id="depositor", dag=dag)

var_environmentally_preferable_procurements_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/environmentally-preferable-procurements/transform.py", task_id="transform", dag=dag)

var_inmate_admissions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-admissions/depositor.py", task_id="depositor", dag=dag)

var_sidewalk_café_regulations_gis_geodatabase_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk-café-regulations-gis-geodatabase/depositor.py", task_id="depositor", dag=dag)

var_sidewalk_café_regulations_gis_geodatabase_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk-café-regulations-gis-geodatabase/transform.py", task_id="transform", dag=dag)

var_dycd_after_school_programs_healthy_families_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-healthy-families/depositor.py", task_id="depositor", dag=dag)

var_trained_medallion_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/trained-medallion-drivers/depositor.py", task_id="depositor", dag=dag)

var_times_square_property_data_commercial_and_retail_properties_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/times-square-property-data-commercial-and-retail-properties/depositor.py", task_id="depositor", dag=dag)

var_cash_assistance_recipients_in_nyc_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cash-assistance-recipients-in-nyc/depositor.py", task_id="depositor", dag=dag)

var_procurements_by_size_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/procurements-by-size/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_other_bureaus_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-other-bureaus-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_bronx_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-bronx-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_organized_crime_control_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-organized-crime-control-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_underutilized_space_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/underutilized-space-report/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_supervision_intakes_by_calendar_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-supervision-intakes-by-calendar-year/depositor.py", task_id="depositor", dag=dag)

var_most_popular_baby_names_by_sex_and_mothers_ethnic_group_new_york_city_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/most-popular-baby-names-by-sex-and-mothers-ethnic-group-new-york-city/depositor.py", task_id="depositor", dag=dag)

var_average_days_for_the_ccrb_to_close_case_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/average-days-for-the-ccrb-to-close-case/depositor.py", task_id="depositor", dag=dag)

var_2010_census_tract_to_neighborhood_tabulation_area_equivalency_table_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2010-census-tract-to-neighborhood-tabulation-area-equivalency-table/depositor.py", task_id="depositor", dag=dag)

var_directory_of_parks_disability_accessibility_facilities_and_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-parks-disability-accessibility-facilities-and-programs/depositor.py", task_id="depositor", dag=dag)

var_botanical_gardens_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/botanical-gardens/depositor.py", task_id="depositor", dag=dag)

var_school_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-districts/depositor.py", task_id="depositor", dag=dag)

var_property_valuation_and_assessment_data_tax_classes_234_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-valuation-and-assessment-data-tax-classes-234/depositor.py", task_id="depositor", dag=dag)

var_property_valuation_and_assessment_data_tax_classes_234_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-valuation-and-assessment-data-tax-classes-234/transform.py", task_id="transform", dag=dag)

var_directory_of_city_resources_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-city-resources/depositor.py", task_id="depositor", dag=dag)

var_electric_consumption_and_cost_2010_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/electric-consumption-and-cost-2010-2016/depositor.py", task_id="depositor", dag=dag)

var_press_releases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/press-releases/depositor.py", task_id="depositor", dag=dag)

var_press_releases_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/press-releases/transform.py", task_id="transform", dag=dag)

var_school_attendance_and_enrollment_statistics_by_district_2010_11_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-attendance-and-enrollment-statistics-by-district-2010-11/depositor.py", task_id="depositor", dag=dag)

var_sea_level_rise_maps_2050s_100_year_floodplain_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sea-level-rise-maps-2050s-100-year-floodplain/depositor.py", task_id="depositor", dag=dag)

var_derelict_vehicle_dispositions_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/derelict-vehicle-dispositions-vehicles/depositor.py", task_id="depositor", dag=dag)

var_2000_census_tracts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2000-census-tracts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_summary_of_dbp_quarterly_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/summary-of-dbp-quarterly-report/depositor.py", task_id="depositor", dag=dag)

var_report_on_youth_in_foster_care_ll_46_2015_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/report-on-youth-in-foster-care-ll-46-2015/depositor.py", task_id="depositor", dag=dag)

var_report_on_youth_in_foster_care_ll_46_2015_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/report-on-youth-in-foster-care-ll-46-2015/transform.py", task_id="transform", dag=dag)

var_bicycle_parking_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bicycle-parking/depositor.py", task_id="depositor", dag=dag)

var_bicycle_parking_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/bicycle-parking/transform.py", task_id="transform", dag=dag)

var_dof_summary_of_neighborhood_sales_in_queens_for_class_1_2_and_3_family_homes_2005_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2005/depositor.py", task_id="depositor", dag=dag)

var_citywide_auto_fringe_benefits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citywide-auto-fringe-benefits/depositor.py", task_id="depositor", dag=dag)

var_adult_family_health_plus_levels_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/adult-family-health-plus-levels/depositor.py", task_id="depositor", dag=dag)

var_local_law_19_section_612_report_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-19-section-612-report/depositor.py", task_id="depositor", dag=dag)

var_local_law_19_section_612_report_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-19-section-612-report/transform.py", task_id="transform", dag=dag)

var_local_law_44_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-44/depositor.py", task_id="depositor", dag=dag)

var_local_law_44_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/local-law-44/transform.py", task_id="transform", dag=dag)

var_congressional_districts_water_areas_included_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/congressional-districts-water-areas-included/depositor.py", task_id="depositor", dag=dag)

var_dof_building_classification_codes_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-building-classification-codes/depositor.py", task_id="depositor", dag=dag)

var_dof_building_classification_codes_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-building-classification-codes/transform.py", task_id="transform", dag=dag)

var_parking_violations_issued_fiscal_year_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/parking-violations-issued-fiscal-year-2016/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_the_organized_crime_control_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-the-organized-crime-control-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_property_valuation_and_assessment_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-valuation-and-assessment-data/depositor.py", task_id="depositor", dag=dag)

var_property_valuation_and_assessment_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/property-valuation-and-assessment-data/transform.py", task_id="transform", dag=dag)

var_harbor_water_quality_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/harbor-water-quality/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_brooklyn_fy_20082009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-brooklyn-fy-20082009/depositor.py", task_id="depositor", dag=dag)

var_2012_2013_school_zones_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2012-2013-school-zones/depositor.py", task_id="depositor", dag=dag)

var_2012_2013_school_zones_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2012-2013-school-zones/transform.py", task_id="transform", dag=dag)

var_dycd_beacon_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-beacon/depositor.py", task_id="depositor", dag=dag)

var_school_zones_2011_2012_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-zones-2011-2012/depositor.py", task_id="depositor", dag=dag)

var_school_zones_2011_2012_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-zones-2011-2012/transform.py", task_id="transform", dag=dag)

var_hpd_development_team_element_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hpd-development-team-element/depositor.py", task_id="depositor", dag=dag)

var_luxury_limousine_services_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/luxury-limousine-services-bases/depositor.py", task_id="depositor", dag=dag)

var_luxury_limousine_services_bases_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/luxury-limousine-services-bases/transform.py", task_id="transform", dag=dag)

var_inspections_2_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inspections-2/depositor.py", task_id="depositor", dag=dag)

var_census_demographics_at_the_neighborhood_tabulation_area_nta_level_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/census-demographics-at-the-neighborhood-tabulation-area-nta-level/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_borough_classes_of_2005_2011_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-borough-classes-of-2005-2011-swd/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_citywide_for_class_1_2_and_3_family_homes_2007_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-citywide-for-class-1-2-and-3-family-homes-2007/depositor.py", task_id="depositor", dag=dag)

var_hra_special_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hra-special-services/depositor.py", task_id="depositor", dag=dag)

var_nycha_applicant_income_limits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-applicant-income-limits/depositor.py", task_id="depositor", dag=dag)

var_ap_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ap-results/depositor.py", task_id="depositor", dag=dag)

var_school_progress_reports_all_schools_2009_10_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-progress-reports-all-schools-2009-10/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-vehicles/depositor.py", task_id="depositor", dag=dag)

var_yellow_medallion_taxicabs_vehicles_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/yellow-medallion-taxicabs-vehicles/transform.py", task_id="transform", dag=dag)

var_dycd_after_school_programs_isy_in_school_youth_employment_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-isy-in-school-youth-employment-programs/depositor.py", task_id="depositor", dag=dag)

var_fire_companies_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fire-companies/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_probationers_rearrested_as_a_percentage_of_nypd_arrest_report_monthly_average_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-probationers-rearrested-as-a-percentage-of-nypd-arrest-report-monthly-average/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_district_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-district-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_upcoming_contracts_to_be_awarded_cap_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/upcoming-contracts-to-be-awarded-cap/depositor.py", task_id="depositor", dag=dag)

var_cooking_gas_consumption_and_cost_2010_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cooking-gas-consumption-and-cost-2010-2016/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_boro_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-boro-all-students/depositor.py", task_id="depositor", dag=dag)

var_open_balance_staten_island_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-balance-staten-island/depositor.py", task_id="depositor", dag=dag)

var_open_balance_staten_island_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-balance-staten-island/transform.py", task_id="transform", dag=dag)

var_nyc_council_constituent_services_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-council-constituent-services/depositor.py", task_id="depositor", dag=dag)

var_citywide_payroll_data_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citywide-payroll-data-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_trade_waste_broker_registrants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/trade-waste-broker-registrants/depositor.py", task_id="depositor", dag=dag)

var_ready_ny_events_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ready-ny-events/depositor.py", task_id="depositor", dag=dag)

var_social_indicators_report_data_by_neighborhood_tabulation_districts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/social-indicators-report-data-by-neighborhood-tabulation-districts/depositor.py", task_id="depositor", dag=dag)

var_regents_exam_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/regents-exam-results/depositor.py", task_id="depositor", dag=dag)

var_directory_of_dop_family_adult_court_contact_information_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-dop-family-adult-court-contact-information/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_nw_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-nw/depositor.py", task_id="depositor", dag=dag)

var_attribution_of_complaints_to_different_bureaus_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/attribution-of-complaints-to-different-bureaus/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_supervision_passthrough_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-supervision-passthrough-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_street_weekly_resurfacing_schedule_staten_island_staten_island_milling_and_paving_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-weekly-resurfacing-schedule-staten-island-staten-island-milling-and-paving/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_deputy_commissioners_and_miscellaneous_commands_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-deputy-commissioners-and-miscellaneous-commands-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_basketball_courts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-basketball-courts/depositor.py", task_id="depositor", dag=dag)

var_directory_of_basketball_courts_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-basketball-courts/transform.py", task_id="transform", dag=dag)

var_new_york_city_council_discretionary_funding_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-council-discretionary-funding/depositor.py", task_id="depositor", dag=dag)

var_capacity_project_site_location_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/capacity-project-site-location/depositor.py", task_id="depositor", dag=dag)

var_revised_notice_of_property_value_rnopv_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/revised-notice-of-property-value-rnopv/depositor.py", task_id="depositor", dag=dag)

var_dof_summary_of_neighborhood_sales_for_queens_for_class_1_2_and_3_family_homes_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-summary-of-neighborhood-sales-for-queens-for-class-1-2-and-3-family-homes-2009/depositor.py", task_id="depositor", dag=dag)

var_nys_math_test_results_by_grade_2006_2011_citywide_by_race_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nys-math-test-results-by-grade-2006-2011-citywide-by-race-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_dohmh_childcare_center_inspections_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dohmh-childcare-center-inspections/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_offensive_language_allegations_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-offensive-language-allegations-2009/depositor.py", task_id="depositor", dag=dag)

var_education_of_subject_officers_against_whom_allegations_were_substantiated_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/education-of-subject-officers-against-whom-allegations-were-substantiated-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_cool_roofs_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-cool-roofs-buildings/depositor.py", task_id="depositor", dag=dag)

var_center_service_locations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/center-service-locations/depositor.py", task_id="depositor", dag=dag)

var_open_article_7_petitions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-article-7-petitions/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_citywide_by_disability_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-disability-status/depositor.py", task_id="depositor", dag=dag)

var_five_year_plan_summary_by_borough_and_capital_categories_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/five-year-plan-summary-by-borough-and-capital-categories/depositor.py", task_id="depositor", dag=dag)

var_skateparks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/skateparks/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_nda_family_literacy_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-nda-family-literacy/depositor.py", task_id="depositor", dag=dag)

var_fdny_vital_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-vital-statistics/depositor.py", task_id="depositor", dag=dag)

var_directory_of_handball_courts_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-handball-courts/depositor.py", task_id="depositor", dag=dag)

var_directory_of_handball_courts_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-handball-courts/transform.py", task_id="transform", dag=dag)

var_dob_job_application_filings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-job-application-filings/depositor.py", task_id="depositor", dag=dag)

var_referral_centers_for_high_school_alternatives_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/referral-centers-for-high-school-alternatives/depositor.py", task_id="depositor", dag=dag)

var_selected_facilities_and_program_sites_access_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/selected-facilities-and-program-sites-access/depositor.py", task_id="depositor", dag=dag)

var_selected_facilities_and_program_sites_access_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/selected-facilities-and-program-sites-access/transform.py", task_id="transform", dag=dag)

var_broadband_data_dig_datasets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/broadband-data-dig-datasets/depositor.py", task_id="depositor", dag=dag)

var_broadband_data_dig_datasets_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/broadband-data-dig-datasets/transform.py", task_id="transform", dag=dag)

var_water_consumption_and_cost_2013_2016_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/water-consumption-and-cost-2013-2016/depositor.py", task_id="depositor", dag=dag)

var_dob_stalled_construction_sites_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-stalled-construction-sites/depositor.py", task_id="depositor", dag=dag)

var_nycha_resident_data_book_summary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nycha-resident-data-book-summary/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_cases_snapshot_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-cases-snapshot-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_small_business_administration_sba_size_standards_table_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/small-business-administration-sba-size-standards-table/depositor.py", task_id="depositor", dag=dag)

var_green_project_checklist_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/green-project-checklist/depositor.py", task_id="depositor", dag=dag)

var_green_project_checklist_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/green-project-checklist/transform.py", task_id="transform", dag=dag)

var_fdny_fire_department_fire_code_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fdny-fire-department-fire-code-data/depositor.py", task_id="depositor", dag=dag)

var_personal_income_by_agi_range_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/personal-income-by-agi-range/depositor.py", task_id="depositor", dag=dag)

var_leaks_and_their_costs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/leaks-and-their-costs/depositor.py", task_id="depositor", dag=dag)

var_directory_of_barbecuing_areas_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-barbecuing-areas/depositor.py", task_id="depositor", dag=dag)

var_directory_of_barbecuing_areas_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-barbecuing-areas/transform.py", task_id="transform", dag=dag)

var_citiwide_service_desk_statistics_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/citiwide-service-desk-statistics/depositor.py", task_id="depositor", dag=dag)

var_distribution_sites_lcr_monitoring_results_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/distribution-sites-lcr-monitoring-results/depositor.py", task_id="depositor", dag=dag)

var_partners_in_preparedness_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/partners-in-preparedness/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_queens_south_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-queens-south-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_disposition_of_discourtesy_allegations_2008_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/disposition-of-discourtesy-allegations-2008/depositor.py", task_id="depositor", dag=dag)

var_hhs_accelerator_past_procurements_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hhs-accelerator-past-procurements/depositor.py", task_id="depositor", dag=dag)

var_fy16_pmmr_agency_performance_indicators_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/fy16-pmmr-agency-performance-indicators/depositor.py", task_id="depositor", dag=dag)

var_world_trade_center_wtc_patient_categories_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/world-trade-center-wtc-patient-categories/depositor.py", task_id="depositor", dag=dag)

var_traffic_volume_counts_2012_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/traffic-volume-counts-2012-2013/depositor.py", task_id="depositor", dag=dag)

var_projected_population_2010_2040_females_by_age_groups_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-population-2010-2040-females-by-age-groups/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_charter_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-charter-schools/depositor.py", task_id="depositor", dag=dag)

var_community_district_breakdowns_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/community-district-breakdowns/depositor.py", task_id="depositor", dag=dag)

var_manhattan_community_grants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/manhattan-community-grants/depositor.py", task_id="depositor", dag=dag)

var_dob_complaints_received_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-complaints-received/depositor.py", task_id="depositor", dag=dag)

var_emergency_response_incidents_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/emergency-response-incidents/depositor.py", task_id="depositor", dag=dag)

var_street_hail_livery_shl_bases_with_wheelchair_accessible_vehicles_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/street-hail-livery-shl-bases-with-wheelchair-accessible-vehicles/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_staten_island_fy_20102011_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-staten-island-fy-20102011/depositor.py", task_id="depositor", dag=dag)

var_where_incidents_that_led_to_a_complaint_took_place_by_precinct_staten_island_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/where-incidents-that-led-to-a-complaint-took-place-by-precinct-staten-island-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_funded_capacity_seats_and_additional_needs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/funded-capacity-seats-and-additional-needs/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_programs_2013_2014_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-programs-2013-2014/depositor.py", task_id="depositor", dag=dag)

var_staff_injuries_class_a_injuries_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/staff-injuries-class-a-injuries/depositor.py", task_id="depositor", dag=dag)

var_safe_route_to_schools_priority_schools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/safe-route-to-schools-priority-schools/depositor.py", task_id="depositor", dag=dag)

var_energy_usage_from_doe_buildings_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/energy-usage-from-doe-buildings/depositor.py", task_id="depositor", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_district_all_students_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-district-all-students/depositor.py", task_id="depositor", dag=dag)

var_graduation_outcomes_school_level_classes_2010_2011_regents_based_mathela_apm_ethnicity_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-ethnicity/depositor.py", task_id="depositor", dag=dag)

var_inmate_stabbing_slashing_incidents_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-stabbing-slashing-incidents/depositor.py", task_id="depositor", dag=dag)

var_ccrb_assignment_of_officers_against_whom_allegations_were_substantiated_patrol_borough_queens_south_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-queens-south-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_grand_central_partnership_gcp_business_directory_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/grand-central-partnership-gcp-business-directory/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_manhattan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-manhattan/depositor.py", task_id="depositor", dag=dag)

var_municipal_parking_facilities_manhattan_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/municipal-parking-facilities-manhattan/transform.py", task_id="transform", dag=dag)

var_cash_assistance_heads_of_household_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/cash-assistance-heads-of-household/depositor.py", task_id="depositor", dag=dag)

var_hurricane_inundation_zones_ne_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hurricane-inundation-zones-ne/depositor.py", task_id="depositor", dag=dag)

var_dycd_after_school_programs_beacon_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dycd-after-school-programs-beacon-programs/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_intakes_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-intakes-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_open_space_parks_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/open-space-parks/depositor.py", task_id="depositor", dag=dag)

var_hydrography_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/hydrography/depositor.py", task_id="depositor", dag=dag)

var_group_ride_vehicle_pilot_program_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/group-ride-vehicle-pilot-program-drivers/depositor.py", task_id="depositor", dag=dag)

var_group_ride_vehicle_pilot_program_drivers_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/group-ride-vehicle-pilot-program-drivers/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_by_grade_2006_2011_citywide_by_english_proficiency_status_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-english-proficiency-status/depositor.py", task_id="depositor", dag=dag)

var_black_car_services_bases_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/black-car-services-bases/depositor.py", task_id="depositor", dag=dag)

var_black_car_services_bases_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/black-car-services-bases/transform.py", task_id="transform", dag=dag)

var_nyc_school_survey_2008_district_75_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2008-district-75/depositor.py", task_id="depositor", dag=dag)

var_nyc_school_survey_2008_district_75_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-school-survey-2008-district-75/transform.py", task_id="transform", dag=dag)

var_annual_arts_in_school_reports_raw_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annual-arts-in-school-reports-raw-data/depositor.py", task_id="depositor", dag=dag)

var_annual_arts_in_school_reports_raw_data_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/annual-arts-in-school-reports-raw-data/transform.py", task_id="transform", dag=dag)

var_sidewalk_café_regulations_gis_shapefile_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/sidewalk-café-regulations-gis-shapefile/depositor.py", task_id="depositor", dag=dag)

var_dof_condominium_comparable_rental_income_brooklyn_fy_20092010_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dof-condominium-comparable-rental-income-brooklyn-fy-20092010/depositor.py", task_id="depositor", dag=dag)

var_ceqr_projects_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ceqr-projects/depositor.py", task_id="depositor", dag=dag)

var_doe_high_school_directory_2017_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/doe-high-school-directory-2017/depositor.py", task_id="depositor", dag=dag)

var_dop_juvenile_supervision_intakes_by_fiscal_year_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-juvenile-supervision-intakes-by-fiscal-year/depositor.py", task_id="depositor", dag=dag)

var_current_medallion_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/current-medallion-drivers/depositor.py", task_id="depositor", dag=dag)

var_ccrb_average_days_for_the_ccrb_to_close_substantiated_cases_measured_from_date_of_report_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-average-days-for-the-ccrb-to-close-substantiated-cases-measured-from-date-of-report-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_womens_resource_network_database_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-womens-resource-network-database/depositor.py", task_id="depositor", dag=dag)

var_2014_green_taxi_trip_data_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/2014-green-taxi-trip-data/depositor.py", task_id="depositor", dag=dag)

var_projected_new_housing_starts_as_used_in_enrollment_projection_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-new-housing-starts-as-used-in-enrollment-projection/depositor.py", task_id="depositor", dag=dag)

var_nyc_independent_budget_office_ibo_state_and_federal_categorical_aid_fy_1980_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-independent-budget-office-ibo-state-and-federal-categorical-aid-fy-1980-2013/depositor.py", task_id="depositor", dag=dag)

var_dop_adult_investigations_ordered_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dop-adult-investigations-ordered/depositor.py", task_id="depositor", dag=dag)

var_inmate_incidents_slashing_and_stabbing_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/inmate-incidents-slashing-and-stabbing/depositor.py", task_id="depositor", dag=dag)

var_medallion_drivers_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/medallion-drivers/depositor.py", task_id="depositor", dag=dag)

var_wastewater_treatment_plants_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/wastewater-treatment-plants/depositor.py", task_id="depositor", dag=dag)

var_borough_enrollment_offices_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/borough-enrollment-offices/depositor.py", task_id="depositor", dag=dag)

var_directory_of_indoor_swimming_pools_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-indoor-swimming-pools/depositor.py", task_id="depositor", dag=dag)

var_directory_of_indoor_swimming_pools_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-indoor-swimming-pools/transform.py", task_id="transform", dag=dag)

var_approved_registrants_in_the_wholesale_markets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/approved-registrants-in-the-wholesale-markets/depositor.py", task_id="depositor", dag=dag)

var_law_divisions_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/law-divisions/depositor.py", task_id="depositor", dag=dag)

var_projected_population_2010_2040_summary_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/projected-population-2010-2040-summary/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_queens_north_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-queens-north-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_dob_now_build_approved_permits_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/dob-now-build-approved-permits/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_patrol_borough_staten_island_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-patrol-borough-staten-island-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_nyc_open_data_available_datasets_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/nyc-open-data-available-datasets/depositor.py", task_id="depositor", dag=dag)

var_multiple_dwelling_registrations_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/multiple-dwelling-registrations/depositor.py", task_id="depositor", dag=dag)

var_ccrb_attribution_of_complaints_to_the_detective_bureau_2005_2009_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/ccrb-attribution-of-complaints-to-the-detective-bureau-2005-2009/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nature_preserves_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nature-preserves/depositor.py", task_id="depositor", dag=dag)

var_directory_of_nature_preserves_transform = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-nature-preserves/transform.py", task_id="transform", dag=dag)

var_english_language_arts_ela_test_results_2006_2012_borough_gender_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/english-language-arts-ela-test-results-2006-2012-borough-gender/depositor.py", task_id="depositor", dag=dag)

var_non_controllable_agency_expenses_financial_plan_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/non-controllable-agency-expenses-financial-plan/depositor.py", task_id="depositor", dag=dag)

var_math_test_results_2006_2012_school_swd_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/math-test-results-2006-2012-school-swd/depositor.py", task_id="depositor", dag=dag)

var_electronics_stores_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/electronics-stores/depositor.py", task_id="depositor", dag=dag)

var_directory_of_lead_agencies_and_housing_programs_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/directory-of-lead-agencies-and-housing-programs/depositor.py", task_id="depositor", dag=dag)

var_school_based_programs_by_borough_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/school-based-programs-by-borough/depositor.py", task_id="depositor", dag=dag)

var_new_york_city_council_discretionary_funding_2009_2013_depositor = BashOperator(bash_command="python /home/alex/Desktop/urban-physiology-nyc-catalog/tasks/new-york-city-council-discretionary-funding-2009-2013/depositor.py", task_id="depositor", dag=dag)
var_weekend_traffic_updates_transform.set_upstream(var_weekend_traffic_updates_depositor)

var_fiscal_2013_appendices_transform.set_upstream(var_fiscal_2013_appendices_depositor)

var_street_name_dictionary_transform.set_upstream(var_street_name_dictionary_depositor)

var_2014_2015_school_quality_reports_results_for_elementary_middle_and_k_8_schools_transform.set_upstream(var_2014_2015_school_quality_reports_results_for_elementary_middle_and_k_8_schools_depositor)

var_open_balance_bronx_transform.set_upstream(var_open_balance_bronx_depositor)

var_demographics_and_profiles_at_the_public_use_microdata_area_puma_subarea_level_transform.set_upstream(var_demographics_and_profiles_at_the_public_use_microdata_area_puma_subarea_level_depositor)

var_broadway_events_calendar_transform.set_upstream(var_broadway_events_calendar_depositor)

var_lion_differences_file_transform.set_upstream(var_lion_differences_file_depositor)

var_nyc_thru_truck_routes_transform.set_upstream(var_nyc_thru_truck_routes_depositor)

var_commuter_van_services_drivers_transform.set_upstream(var_commuter_van_services_drivers_depositor)

var_2009_school_survey_transform.set_upstream(var_2009_school_survey_depositor)

var_staten_island_ferry_schedule_gtfs_transform.set_upstream(var_staten_island_ferry_schedule_gtfs_depositor)

var_luxury_limousine_services_vehicles_transform.set_upstream(var_luxury_limousine_services_vehicles_depositor)

var_competitiveness_transform.set_upstream(var_competitiveness_depositor)

var_weekday_traffic_updates_transform.set_upstream(var_weekday_traffic_updates_depositor)

var_zoning_gis_data_geodatabase_transform.set_upstream(var_zoning_gis_data_geodatabase_depositor)

var_2040_population_projection_tables_transform.set_upstream(var_2040_population_projection_tables_depositor)

var_nyc_school_survey_2009_transform.set_upstream(var_nyc_school_survey_2009_depositor)

var_nyc_local_truck_routes_transform.set_upstream(var_nyc_local_truck_routes_depositor)

var_directory_of_running_tracks_transform.set_upstream(var_directory_of_running_tracks_depositor)

var_paratransit_services_drivers_transform.set_upstream(var_paratransit_services_drivers_depositor)

var_rudy_w_giuliani_1994_2001_transform.set_upstream(var_rudy_w_giuliani_1994_2001_depositor)

var_yellow_medallion_taxicabs_drivers_who_have_completed_passenger_assistance_training_transform.set_upstream(var_yellow_medallion_taxicabs_drivers_who_have_completed_passenger_assistance_training_depositor)

var_citi_bike_live_station_feed_json_transform.set_upstream(var_citi_bike_live_station_feed_json_depositor)

var_park_closure_notifications_transform.set_upstream(var_park_closure_notifications_depositor)

var_street_network_changes_transform.set_upstream(var_street_network_changes_depositor)

var_detention_and_placement_incident_reports_transform.set_upstream(var_detention_and_placement_incident_reports_depositor)

var_lion_transform.set_upstream(var_lion_depositor)

var_census_demographics_at_the_nyc_city_council_district_cncld_level_transform.set_upstream(var_census_demographics_at_the_nyc_city_council_district_cncld_level_depositor)

var_directory_of_hiking_trails_transform.set_upstream(var_directory_of_hiking_trails_depositor)

var_municipal_parking_facilities_staten_island_transform.set_upstream(var_municipal_parking_facilities_staten_island_depositor)

var_property_address_directory_transform.set_upstream(var_property_address_directory_depositor)

var_directory_of_boating_and_marinas_transform.set_upstream(var_directory_of_boating_and_marinas_depositor)

var_yellow_medallion_taxicabs_drivers_transform.set_upstream(var_yellow_medallion_taxicabs_drivers_depositor)

var_directory_of_dog_runs_and_off_leash_areas_transform.set_upstream(var_directory_of_dog_runs_and_off_leash_areas_depositor)

var_directory_of_cricket_fields_transform.set_upstream(var_directory_of_cricket_fields_depositor)

var_historical_new_york_city_crime_data_transform.set_upstream(var_historical_new_york_city_crime_data_depositor)

var_child_welfare_indicators_annual_and_quarterly_report_indicators_transform.set_upstream(var_child_welfare_indicators_annual_and_quarterly_report_indicators_depositor)

var_facilities_database_facdb_supplemental_file_package_transform.set_upstream(var_facilities_database_facdb_supplemental_file_package_depositor)

var_wastewater_treatment_plant_performance_data_transform.set_upstream(var_wastewater_treatment_plant_performance_data_depositor)

var_outcome_of_preventive_cases_closed_by_borough_and_cd_cy_2014_transform.set_upstream(var_outcome_of_preventive_cases_closed_by_borough_and_cd_cy_2014_depositor)

var_filming_locations_scenes_from_the_city_transform.set_upstream(var_filming_locations_scenes_from_the_city_depositor)

var_nyc_school_survey_2007_transform.set_upstream(var_nyc_school_survey_2007_depositor)

var_parking_regulation_locations_and_signs_transform.set_upstream(var_parking_regulation_locations_and_signs_depositor)

var_board_of_education_1934_2002_transform.set_upstream(var_board_of_education_1934_2002_depositor)

var_directory_of_concessions_transform.set_upstream(var_directory_of_concessions_depositor)

var_waterfront_revitalization_program_transform.set_upstream(var_waterfront_revitalization_program_depositor)

var_for_hire_vehicle_fhv_drivers_transform.set_upstream(var_for_hire_vehicle_fhv_drivers_depositor)

var_yellow_medallion_taxicabs_brokers_transform.set_upstream(var_yellow_medallion_taxicabs_brokers_depositor)

var_new_preventive_cases_opened_by_borough_and_cd_cy_15_transform.set_upstream(var_new_preventive_cases_opened_by_borough_and_cd_cy_15_depositor)

var_directory_of_tennis_courts_transform.set_upstream(var_directory_of_tennis_courts_depositor)

var_directory_of_horseback_riding_trails_transform.set_upstream(var_directory_of_horseback_riding_trails_depositor)

var_museums_and_galleries_transform.set_upstream(var_museums_and_galleries_depositor)

var_real_time_traffic_speed_data_transform.set_upstream(var_real_time_traffic_speed_data_depositor)

var_procurement_by_method_transform.set_upstream(var_procurement_by_method_depositor)

var_foursquare_api_transform.set_upstream(var_foursquare_api_depositor)

var_adopt_a_tree_inventory_transform.set_upstream(var_adopt_a_tree_inventory_depositor)

var_paratransit_services_vehicles_transform.set_upstream(var_paratransit_services_vehicles_depositor)

var_chancellor_of_nyc_board_of_education_1970_1989_transform.set_upstream(var_chancellor_of_nyc_board_of_education_1970_1989_depositor)

var_yellow_medallion_taxicabs_agents_transform.set_upstream(var_yellow_medallion_taxicabs_agents_depositor)

var_weekly_resurfacing_schedule_transform.set_upstream(var_weekly_resurfacing_schedule_depositor)

var_privately_owned_public_spaces_transform.set_upstream(var_privately_owned_public_spaces_depositor)

var_bicycle_shelters_transform.set_upstream(var_bicycle_shelters_depositor)

var_city_owned_and_leased_property_colp_transform.set_upstream(var_city_owned_and_leased_property_colp_depositor)

var_municipal_parking_facilities_queens_transform.set_upstream(var_municipal_parking_facilities_queens_depositor)

var_bike_counts_transform.set_upstream(var_bike_counts_depositor)

var_new_york_tech_ecosystem_report_data_transform.set_upstream(var_new_york_tech_ecosystem_report_data_depositor)

var_2010_school_survey_transform.set_upstream(var_2010_school_survey_depositor)

var_nyc_truck_routes_transform.set_upstream(var_nyc_truck_routes_depositor)

var_municipal_parking_facilities_brooklyn_transform.set_upstream(var_municipal_parking_facilities_brooklyn_depositor)

var_zip_code_boundaries_transform.set_upstream(var_zip_code_boundaries_depositor)

var_nyc_school_survey_2008_general_education_transform.set_upstream(var_nyc_school_survey_2008_general_education_depositor)

var_school_point_locations_transform.set_upstream(var_school_point_locations_depositor)

var_franchise_and_concession_review_committee_transform.set_upstream(var_franchise_and_concession_review_committee_depositor)

var_abuseneglect_by_community_district_cd_transform.set_upstream(var_abuseneglect_by_community_district_cd_depositor)

var_open_balance_manhattan_transform.set_upstream(var_open_balance_manhattan_depositor)

var_nyc_school_survey_2011_transform.set_upstream(var_nyc_school_survey_2011_depositor)

var_placements_by_community_district_cd_transform.set_upstream(var_placements_by_community_district_cd_depositor)

var_selected_facilities_and_program_sites_text_transform.set_upstream(var_selected_facilities_and_program_sites_text_depositor)

var_yellow_medallion_taxicabs_metershops_transform.set_upstream(var_yellow_medallion_taxicabs_metershops_depositor)

var_demographics_and_profiles_at_the_neighborhood_tabulation_area_nta_level_transform.set_upstream(var_demographics_and_profiles_at_the_neighborhood_tabulation_area_nta_level_depositor)

var_commuter_van_services_vehicles_transform.set_upstream(var_commuter_van_services_vehicles_depositor)

var_special_traffic_updates_transform.set_upstream(var_special_traffic_updates_depositor)

var_nyc_parks_public_events_upcoming_14_days_transform.set_upstream(var_nyc_parks_public_events_upcoming_14_days_depositor)

var_dep_green_infrastructure_transform.set_upstream(var_dep_green_infrastructure_depositor)

var_annual_report_statistics_transform.set_upstream(var_annual_report_statistics_depositor)

var_new_york_city_street_reconstruction_10_year_plan_transform.set_upstream(var_new_york_city_street_reconstruction_10_year_plan_depositor)

var_new_york_city_water_trail_kayak_and_canoe_launch_sites_transform.set_upstream(var_new_york_city_water_trail_kayak_and_canoe_launch_sites_depositor)

var_citywide_low_bridges_transform.set_upstream(var_citywide_low_bridges_depositor)

var_directory_of_public_computer_resource_centers_transform.set_upstream(var_directory_of_public_computer_resource_centers_depositor)

var_ccr_annual_report_2_transform.set_upstream(var_ccr_annual_report_2_depositor)

var_nyccas_air_pollution_rasters_transform.set_upstream(var_nyccas_air_pollution_rasters_depositor)

var_2014_2015_school_quality_reports_results_for_high_schools_transform.set_upstream(var_2014_2015_school_quality_reports_results_for_high_schools_depositor)

var_directory_of_temporary_public_art_transform.set_upstream(var_directory_of_temporary_public_art_depositor)

var_directory_of_eateries_transform.set_upstream(var_directory_of_eateries_depositor)

var_recording_studios_transform.set_upstream(var_recording_studios_depositor)

var_clean_air_survey_content_2009_transform.set_upstream(var_clean_air_survey_content_2009_depositor)

var_bicycle_counts_for_east_river_bridges_transform.set_upstream(var_bicycle_counts_for_east_river_bridges_depositor)

var_greenstreets_transform.set_upstream(var_greenstreets_depositor)

var_directory_of_ice_skating_rinks_transform.set_upstream(var_directory_of_ice_skating_rinks_depositor)

var_land_acquisition_statistics_transform.set_upstream(var_land_acquisition_statistics_depositor)

var_directory_of_nature_centers_transform.set_upstream(var_directory_of_nature_centers_depositor)

var_annual_procurement_indicator_report_fy15_transform.set_upstream(var_annual_procurement_indicator_report_fy15_depositor)

var_paratransit_services_bases_transform.set_upstream(var_paratransit_services_bases_depositor)

var_unaffiliated_vehicles_transform.set_upstream(var_unaffiliated_vehicles_depositor)

var_black_car_services_vehicles_transform.set_upstream(var_black_car_services_vehicles_depositor)

var_directory_of_beaches_transform.set_upstream(var_directory_of_beaches_depositor)

var_directory_of_zoos_and_aquariums_transform.set_upstream(var_directory_of_zoos_and_aquariums_depositor)

var_government_issued_personal_identification_for_youth_in_foster_care_transform.set_upstream(var_government_issued_personal_identification_for_youth_in_foster_care_depositor)

var_directory_of_bocce_courts_transform.set_upstream(var_directory_of_bocce_courts_depositor)

var_nyc_school_survey_2010_transform.set_upstream(var_nyc_school_survey_2010_depositor)

var_community_car_services_livery_vehicles_transform.set_upstream(var_community_car_services_livery_vehicles_depositor)

var_open_summonses_active_for_hire_vehicle_fhv_owners_transform.set_upstream(var_open_summonses_active_for_hire_vehicle_fhv_owners_depositor)

var_alliance_for_downtown_new_york_big_apps_data_transform.set_upstream(var_alliance_for_downtown_new_york_big_apps_data_depositor)

var_landcover_raster_data_2010_transform.set_upstream(var_landcover_raster_data_2010_depositor)

var_detention_and_placement_demographic_reports_transform.set_upstream(var_detention_and_placement_demographic_reports_depositor)

var_municipal_parking_facilities_bronx_transform.set_upstream(var_municipal_parking_facilities_bronx_depositor)

var_detention_and_placement_abuseneglect_reports_transform.set_upstream(var_detention_and_placement_abuseneglect_reports_depositor)

var_times_square_pedestrian_counts_transform.set_upstream(var_times_square_pedestrian_counts_depositor)

var_census_demographics_at_the_nyc_community_district_cd_level_transform.set_upstream(var_census_demographics_at_the_nyc_community_district_cd_level_depositor)

var_parks_inspections_data_transform.set_upstream(var_parks_inspections_data_depositor)

var_directory_of_historic_houses_transform.set_upstream(var_directory_of_historic_houses_depositor)

var_property_valuation_and_assessment_data_tax_class_transform.set_upstream(var_property_valuation_and_assessment_data_tax_class_depositor)

var_directory_of_recreation_centers_transform.set_upstream(var_directory_of_recreation_centers_depositor)

var_annualized_rolling_sales_update_transform.set_upstream(var_annualized_rolling_sales_update_depositor)

var_group_ride_vehicle_pilot_program_bases_transform.set_upstream(var_group_ride_vehicle_pilot_program_bases_depositor)

var_city_bench_locations_transform.set_upstream(var_city_bench_locations_depositor)

var_roadbed_pointer_list_rpl_transform.set_upstream(var_roadbed_pointer_list_rpl_depositor)

var_community_car_services_livery_bases_transform.set_upstream(var_community_car_services_livery_bases_depositor)

var_local_law_1_city_council_report_fy_2015_transform.set_upstream(var_local_law_1_city_council_report_fy_2015_depositor)

var_directory_of_playgrounds_transform.set_upstream(var_directory_of_playgrounds_depositor)

var_high_school_graduation_rates_of_youth_in_foster_care_annual_report_2015_transform.set_upstream(var_high_school_graduation_rates_of_youth_in_foster_care_annual_report_2015_depositor)

var_group_ride_vehicle_pilot_program_vehicles_transform.set_upstream(var_group_ride_vehicle_pilot_program_vehicles_depositor)

var_sustainability_indicators_2012_2_transform.set_upstream(var_sustainability_indicators_2012_2_depositor)

var_directory_historical_signs_transform.set_upstream(var_directory_historical_signs_depositor)

var_environmentally_preferable_procurements_transform.set_upstream(var_environmentally_preferable_procurements_depositor)

var_sidewalk_café_regulations_gis_geodatabase_transform.set_upstream(var_sidewalk_café_regulations_gis_geodatabase_depositor)

var_property_valuation_and_assessment_data_tax_classes_234_transform.set_upstream(var_property_valuation_and_assessment_data_tax_classes_234_depositor)

var_press_releases_transform.set_upstream(var_press_releases_depositor)

var_report_on_youth_in_foster_care_ll_46_2015_transform.set_upstream(var_report_on_youth_in_foster_care_ll_46_2015_depositor)

var_bicycle_parking_transform.set_upstream(var_bicycle_parking_depositor)

var_local_law_19_section_612_report_transform.set_upstream(var_local_law_19_section_612_report_depositor)

var_local_law_44_transform.set_upstream(var_local_law_44_depositor)

var_dof_building_classification_codes_transform.set_upstream(var_dof_building_classification_codes_depositor)

var_property_valuation_and_assessment_data_transform.set_upstream(var_property_valuation_and_assessment_data_depositor)

var_2012_2013_school_zones_transform.set_upstream(var_2012_2013_school_zones_depositor)

var_school_zones_2011_2012_transform.set_upstream(var_school_zones_2011_2012_depositor)

var_luxury_limousine_services_bases_transform.set_upstream(var_luxury_limousine_services_bases_depositor)

var_yellow_medallion_taxicabs_vehicles_transform.set_upstream(var_yellow_medallion_taxicabs_vehicles_depositor)

var_open_balance_staten_island_transform.set_upstream(var_open_balance_staten_island_depositor)

var_directory_of_basketball_courts_transform.set_upstream(var_directory_of_basketball_courts_depositor)

var_directory_of_handball_courts_transform.set_upstream(var_directory_of_handball_courts_depositor)

var_selected_facilities_and_program_sites_access_transform.set_upstream(var_selected_facilities_and_program_sites_access_depositor)

var_broadband_data_dig_datasets_transform.set_upstream(var_broadband_data_dig_datasets_depositor)

var_green_project_checklist_transform.set_upstream(var_green_project_checklist_depositor)

var_directory_of_barbecuing_areas_transform.set_upstream(var_directory_of_barbecuing_areas_depositor)

var_municipal_parking_facilities_manhattan_transform.set_upstream(var_municipal_parking_facilities_manhattan_depositor)

var_group_ride_vehicle_pilot_program_drivers_transform.set_upstream(var_group_ride_vehicle_pilot_program_drivers_depositor)

var_black_car_services_bases_transform.set_upstream(var_black_car_services_bases_depositor)

var_nyc_school_survey_2008_district_75_transform.set_upstream(var_nyc_school_survey_2008_district_75_depositor)

var_annual_arts_in_school_reports_raw_data_transform.set_upstream(var_annual_arts_in_school_reports_raw_data_depositor)

var_directory_of_indoor_swimming_pools_transform.set_upstream(var_directory_of_indoor_swimming_pools_depositor)

var_directory_of_nature_preserves_transform.set_upstream(var_directory_of_nature_preserves_depositor)
