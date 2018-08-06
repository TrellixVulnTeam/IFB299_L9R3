SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CarRentalCompany`
--

-- --------------------------------------------------------

--
-- Table structure for table `Cars`
--

CREATE TABLE `Cars` (
  `Car_ID` int(11) NOT NULL,
  `Car_MakeName` varchar(30) NOT NULL,
  `Car_Model` varchar(30) NOT NULL,
  `Car_Series` varchar(10) NOT NULL,
  `Car_SeriesYear` varchar(4) NOT NULL,
  `Car_PriceNew` int(11) NOT NULL,
  `Car_EngineSize` varchar(5) NOT NULL,
  `Car_FuelSystem` varchar(20) NOT NULL,
  `Car_TankCapacity` varchar(5) NOT NULL,
  `Car_Power` varchar(10) NOT NULL,
  `Car_SeatingCapacity` tinyint(1) NOT NULL,
  `Car_StandardTransmission` varchar(6) NOT NULL,
  `Car_BodyType` varchar(12) NOT NULL,
  `Car_Drive` varchar(5) NOT NULL,
  `Car_Wheelbase` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Customers`
--

CREATE TABLE `Customers` (
  `Customer_ID` int(11) NOT NULL,
  `Customer_Name` varchar(50) NOT NULL,
  `Customer_Phone` varchar(21) NOT NULL,
  `Customer_Address` varchar(255) NOT NULL,
  `Customer_Birthday` date NOT NULL,
  `Customer_Occupation` varchar(20) NOT NULL,
  `Customer_Gender` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `OrderID` int(11) NOT NULL,
  `Order_CreateDate` date NOT NULL,
  `Customer_ID` int(11) NOT NULL,
  `Car_ID` int(11) NOT NULL,
  `Order_PickupDate` date NOT NULL,
  `Order_PickupStoreID` int(11) NOT NULL,
  `Order_ReturnDate` date NOT NULL,
  `Order_ReturnStoreID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Stores`
--

CREATE TABLE `Stores` (
  `Store_ID` int(11) NOT NULL,
  `Store_Name` varchar(50) NOT NULL,
  `Store_Address` varchar(255) NOT NULL,
  `Store_Phone` varchar(21) NOT NULL,
  `Store_City` varchar(50) NOT NULL,
  `Store_State_Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Cars`
--
ALTER TABLE `Cars`
  ADD PRIMARY KEY (`Car_ID`);

--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`OrderID`);

--
-- Indexes for table `Stores`
--
ALTER TABLE `Stores`
  ADD PRIMARY KEY (`Store_ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
