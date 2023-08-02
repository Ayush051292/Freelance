-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 13, 2023 at 03:00 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rrchrmsserver`
--

-- --------------------------------------------------------

--
-- Table structure for table `clienttypemasters`
--

CREATE TABLE `clienttypemasters` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `w_from` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `w_to` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `w_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `v_from` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `v_to` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `v_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_by` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `modified_by` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clienttypemasters`
--
ALTER TABLE `clienttypemasters`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clienttypemasters`
--
ALTER TABLE `clienttypemasters`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
