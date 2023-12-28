

```MYSQL
CREATE TABLE `appointments` (

  `AppointmentID` int NOT NULL,

  `DoctorID` int DEFAULT NULL,

  `PatientID` int DEFAULT NULL,

  `AppointmentDateTime` datetime DEFAULT NULL,

  PRIMARY KEY (`AppointmentID`),

  KEY `DoctorID` (`DoctorID`),

  KEY `PatientID` (`PatientID`),

  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`DoctorID`) REFERENCES `doctors` (`DoctorID`),

  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`)

)

  
  

CREATE TABLE `doctors` (

  `DoctorID` int NOT NULL,

  `FirstName` varchar(50) DEFAULT NULL,

  `LastName` varchar(50) DEFAULT NULL,

  `Gender` varchar(10) DEFAULT NULL,

  `DateOfBirth` date DEFAULT NULL,

  `PhoneNumber` varchar(30) DEFAULT NULL,

  `Address` varchar(200) DEFAULT NULL,

  `City` varchar(100) DEFAULT NULL,

  `State` varchar(100) DEFAULT NULL,

  `Country` varchar(100) DEFAULT NULL,

  `PostalCode` varchar(20) DEFAULT NULL,

  `Specialization` varchar(100) DEFAULT NULL,

  `UserID` int DEFAULT NULL,

  PRIMARY KEY (`DoctorID`),

  KEY `UserID` (`UserID`),

  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `login` (`UserID`)

)

  
  

CREATE TABLE `insurancecompanies` (

  `CompanyID` int NOT NULL,

  `CompanyName` varchar(100) DEFAULT NULL,

  `Address` varchar(200) DEFAULT NULL,

  `City` varchar(100) DEFAULT NULL,

  `State` varchar(100) DEFAULT NULL,

  `Country` varchar(100) DEFAULT NULL,

  `PostalCode` varchar(20) DEFAULT NULL,

  PRIMARY KEY (`CompanyID`)

)

  
  

CREATE TABLE `insurancepolicies` (

  `PolicyID` int NOT NULL,

  `CompanyID` int DEFAULT NULL,

  `PatientID` int DEFAULT NULL,

  `PolicyNumber` varchar(50) DEFAULT NULL,

  `ExpiryDate` datetime DEFAULT NULL,

  PRIMARY KEY (`PolicyID`),

  KEY `CompanyID` (`CompanyID`),

  KEY `PatientID` (`PatientID`),

  CONSTRAINT `insurancepolicies_ibfk_1` FOREIGN KEY (`CompanyID`) REFERENCES `insurancecompanies` (`CompanyID`),

  CONSTRAINT `insurancepolicies_ibfk_2` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`)

)

  
  

CREATE TABLE `labresults` (

  `ResultID` int NOT NULL,

  `LabTestID` int DEFAULT NULL,

  `PatientID` int DEFAULT NULL,

  `Result` text,

  `ResultValue` decimal(10,2) DEFAULT NULL,

  PRIMARY KEY (`ResultID`),

  KEY `labresults_ibfk_2_idx` (`PatientID`),

  KEY `labresults_ibfk_4` (`LabTestID`),

  CONSTRAINT `labresults_ibfk_4` FOREIGN KEY (`LabTestID`) REFERENCES `labtests` (`TestID`),

  CONSTRAINT `labresults_ibfk_5` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`)

)

  
  

CREATE TABLE `labtests` (

  `TestID` int NOT NULL,

  `TestName` varchar(100) DEFAULT NULL,

  PRIMARY KEY (`TestID`)

)

  
  

CREATE TABLE `login` (

  `UserID` int NOT NULL,

  `Username` varchar(50) DEFAULT NULL,

  `Password` varchar(50) DEFAULT NULL,

  PRIMARY KEY (`UserID`)

)

  
  

CREATE TABLE `medicalrecords` (

  `RecordID` int NOT NULL,

  `PatientID` int DEFAULT NULL,

  `DoctorID` int DEFAULT NULL,

  `AppointmentID` int DEFAULT NULL,

  `Diagnosis` varchar(100) DEFAULT NULL,

  `Treatment` varchar(100) DEFAULT NULL,

  PRIMARY KEY (`RecordID`),

  KEY `PatientID` (`PatientID`),

  KEY `DoctorID` (`DoctorID`),

  KEY `medicalrecords_ibfk_3_idx` (`AppointmentID`),

  CONSTRAINT `medicalrecords_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`),

  CONSTRAINT `medicalrecords_ibfk_2` FOREIGN KEY (`DoctorID`) REFERENCES `doctors` (`DoctorID`),

  CONSTRAINT `medicalrecords_ibfk_3` FOREIGN KEY (`AppointmentID`) REFERENCES `appointments` (`AppointmentID`)

)

  
  

CREATE TABLE `medications` (

  `MedicationID` int NOT NULL,

  `MedicationName` varchar(100) DEFAULT NULL,

  PRIMARY KEY (`MedicationID`)

)

  
  

CREATE TABLE `patients` (

  `PatientID` int NOT NULL,

  `FirstName` varchar(50) DEFAULT NULL,

  `LastName` varchar(50) DEFAULT NULL,

  `Gender` varchar(10) DEFAULT NULL,

  `DateOfBirth` date DEFAULT NULL,

  `PhoneNumber` varchar(30) DEFAULT NULL,

  `Address` varchar(200) DEFAULT NULL,

  `City` varchar(100) DEFAULT NULL,

  `State` varchar(100) DEFAULT NULL,

  `Country` varchar(100) DEFAULT NULL,

  `PostalCode` varchar(20) DEFAULT NULL,

  `UserID` int DEFAULT NULL,

  PRIMARY KEY (`PatientID`),

  KEY `UserID` (`UserID`)

)

  
  

CREATE TABLE `payments` (

  `PaymentID` int NOT NULL,

  `PatientID` int DEFAULT NULL,

  `Amount` decimal(10,2) DEFAULT NULL,

  `PaymentDate` date DEFAULT NULL,

  PRIMARY KEY (`PaymentID`),

  KEY `PatientID` (`PatientID`),

  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`)

)

  
  

CREATE TABLE `prescriptionmedications` (

  `PrescriptionID` int DEFAULT NULL,

  `MedicationID` int DEFAULT NULL,

  `Dosage` varchar(50) DEFAULT NULL,

  `Frequency` varchar(45) DEFAULT NULL,

  KEY `MedicationID` (`MedicationID`),

  KEY `prescriptionmedications_ibfk_1` (`PrescriptionID`),

  CONSTRAINT `prescriptionmedications_ibfk_1` FOREIGN KEY (`PrescriptionID`) REFERENCES `prescriptions` (`PrescriptionID`),

  CONSTRAINT `prescriptionmedications_ibfk_2` FOREIGN KEY (`MedicationID`) REFERENCES `medications` (`MedicationID`)

)

  
  

CREATE TABLE `prescriptions` (

  `PrescriptionID` int NOT NULL,

  `DoctorID` int DEFAULT NULL,

  `PatientID` int DEFAULT NULL,

  `AppointmentID` int DEFAULT NULL,

  `PrescriptionDate` date DEFAULT NULL,

  PRIMARY KEY (`PrescriptionID`),

  KEY `DoctorID` (`DoctorID`),

  KEY `PatientID` (`PatientID`),

  KEY `AppointmentID` (`AppointmentID`),

  CONSTRAINT `prescriptions_ibfk_1` FOREIGN KEY (`DoctorID`) REFERENCES `doctors` (`DoctorID`),

  CONSTRAINT `prescriptions_ibfk_2` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`),

  CONSTRAINT `prescriptions_ibfk_3` FOREIGN KEY (`AppointmentID`) REFERENCES `appointments` (`AppointmentID`)

)
```




0