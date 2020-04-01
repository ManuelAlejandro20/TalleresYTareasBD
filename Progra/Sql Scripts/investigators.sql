-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 09-03-2020 a las 06:49:19
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sciencelair`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `investigators`
--

CREATE TABLE `investigators` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `passportnumber` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `state` enum('ACTIVO','INACTIVO') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'ACTIVO',
  `associatedunit` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `investigators`
--

INSERT INTO `investigators` (`id`, `name`, `passportnumber`, `state`, `associatedunit`, `created_at`, `updated_at`) VALUES
(1, 'MANUEL ALEJANDRO TRIGO MONTALBáN', 'aaa123', 'ACTIVO', 'UNIVERSIDAD DE PALERMO', '2020-03-06 06:37:32', '2020-03-06 06:37:32'),
(2, 'NAOMI ALISON ANDREA CHAVEZ OSORIO', '3dfdf333', 'ACTIVO', 'UCH', '2020-03-06 06:38:19', '2020-03-06 06:38:19'),
(3, 'ANA MERCEDES MONTALBAN FLORES', 'numeroxd', 'ACTIVO', 'UA', '2020-03-06 06:39:16', '2020-03-06 06:39:16'),
(4, 'MANUEL JESUS TRIGO TABORGA', 'aaa123', 'INACTIVO', 'UNIVERSIDAD DE PALERMO', '2020-03-06 06:39:46', '2020-03-06 06:39:46'),
(5, 'CELESTE ROJELIA BLANCO NEGRETE', 'colores123', 'ACTIVO', 'UCN', '2020-03-06 06:41:20', '2020-03-06 06:41:20'),
(6, 'NOELIA ARAYA ROJAS MARTINEZ', '2323ssssdd', 'INACTIVO', 'UNIVERSIDAD DE PALERMO', '2020-03-06 06:44:25', '2020-03-06 06:44:25'),
(7, 'RODRIGO ROBERTO ROJERLIO RODRIGUEZ', 'aaa123', 'ACTIVO', 'UCN', '2020-03-06 07:41:07', '2020-03-06 07:41:07');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `investigators`
--
ALTER TABLE `investigators`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `investigators_name_unique` (`name`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `investigators`
--
ALTER TABLE `investigators`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
