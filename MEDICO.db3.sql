BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "patients" (
	"p_id"	INTEGER,
	"f_name"	TEXT NOT NULL,
	"l_name"	TEXT NOT NULL,
	"age"	TEXT NOT NULL,
	"sex"	TEXT NOT NULL,
	"phone"	TEXT NOT NULL,
	"address"	TEXT NOT NULL,
	"email"	TEXT,
	"reg_date"	TEXT NOT NULL,
	"date_of_departure"	TEXT,
	"reference"	TEXT,
	"complain"	TEXT,
	"blood_diseases"	TEXT NOT NULL,
	"smoker"	TEXT NOT NULL,
	"bleeding_disorder"	TEXT NOT NULL,
	"hepatitis"	TEXT NOT NULL,
	"diabetes"	TEXT NOT NULL,
	"epilepsy"	TEXT NOT NULL,
	"kidney_cardiac_diseases"	TEXT NOT NULL,
	"abnormal_bp"	TEXT NOT NULL,
	"currently_medicated"	TEXT NOT NULL,
	"respiratory_diseases"	TEXT NOT NULL,
	"gum_bleed_brush"	TEXT NOT NULL,
	"allergies"	TEXT NOT NULL,
	"nervous"	TEXT NOT NULL,
	"pregnant"	TEXT NOT NULL,
	"breastfeeding"	TEXT NOT NULL,
	"none_prb_above"	TEXT NOT NULL,
	"med_find_"	TEXT NOT NULL,
	PRIMARY KEY("p_id")
);
CREATE TABLE IF NOT EXISTS "dentists" (
	"d_id"	INTEGER NOT NULL,
	"d_f_name"	TEXT NOT NULL,
	"d_l_name"	TEXT NOT NULL,
	"d_email"	TEXT NOT NULL,
	"d_phone"	INTEGER NOT NULL,
	"d_dob"	TEXT NOT NULL,
	"d_joindate"	TEXT NOT NULL,
	"d_retiredate"	TEXT,
	PRIMARY KEY("d_id")
);
CREATE TABLE IF NOT EXISTS "dentist_availability" (
	"d_id"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	"chk_in"	TEXT,
	"chk_out"	TEXT,
	FOREIGN KEY("d_id") REFERENCES "dentists"("d_id")
);
CREATE TABLE IF NOT EXISTS "payment_history" (
	"payment_id"	INTEGER NOT NULL,
	"p_id"	INTEGER NOT NULL,
	"payment_date"	TEXT NOT NULL,
	"payment_amount"	INTEGER NOT NULL,
	"payment_remarks"	TEXT NOT NULL,
	FOREIGN KEY("p_id") REFERENCES "patients"("p_id"),
	PRIMARY KEY("payment_id")
);
CREATE TABLE IF NOT EXISTS "appointments" (
	"appnt_date"	TEXT NOT NULL,
	"visitor_name"	TEXT NOT NULL,
	"visitor_phone"	TEXT NOT NULL,
	"visit_time"	TEXT NOT NULL,
	"visit_date"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "expense" (
	"expense_date"	TEXT,
	"expense_amount"	TEXT,
	"expense_description"	TEXT
);
COMMIT;
