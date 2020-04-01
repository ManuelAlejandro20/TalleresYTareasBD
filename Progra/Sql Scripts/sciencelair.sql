-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 09-03-2020 a las 06:49:45
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
-- Estructura de tabla para la tabla `country_units`
--

CREATE TABLE `country_units` (
  `namegroup` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `unit` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `country_units`
--

INSERT INTO `country_units` (`namegroup`, `unit`, `country`, `created_at`, `updated_at`) VALUES
('ANTILACRAS', 'UCN', 'CHILE', '2020-03-06 05:38:21', '2020-03-06 05:38:21'),
('ANTILACRAS', 'UA', 'CHILE', '2020-03-06 05:38:21', '2020-03-06 05:38:21'),
('ANTILACRAS', 'UC', 'CHILE', '2020-03-06 05:38:21', '2020-03-06 05:38:21'),
('LOSSOCIEDAD', 'UNIVERSIDAD DE PALERMO', 'ARGENTINA', '2020-03-06 05:40:56', '2020-03-06 05:40:56'),
('LOSSOCIEDAD', 'UCH', 'CHILE', '2020-03-06 05:40:56', '2020-03-06 05:40:56'),
('LOSSOCIEDAD', 'UA', 'CHILE', '2020-03-06 05:40:56', '2020-03-06 05:40:56');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `groups`
--

CREATE TABLE `groups` (
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `path` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `groups`
--

INSERT INTO `groups` (`name`, `path`, `created_at`, `updated_at`) VALUES
('ANTILACRAS', NULL, '2020-03-06 05:38:21', '2020-03-06 05:38:21'),
('LOSSOCIEDAD', '1375713944.jpg', '2020-03-06 05:40:56', '2020-03-06 05:40:56');

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_users_table', 1),
(2, '2014_10_12_100000_create_password_resets_table', 1),
(3, '2020_02_01_215630_create_groups_table', 1),
(4, '2020_02_01_215846_create_country_units_table', 1),
(5, '2020_02_03_040248_create_investigators_table', 1),
(6, '2020_02_05_051152_create_projects_table', 1),
(7, '2020_02_05_051342_create_project__invs_table', 1),
(8, '2020_02_09_221028_create_publications_table', 1),
(9, '2020_02_09_222042_create_publication_invs_table', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `password_resets`
--

CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `projects`
--

CREATE TABLE `projects` (
  `name_project` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `state` enum('EN EJECUCION','FINALIZADO','CANCELADO') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'EN EJECUCION',
  `date_start` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_end` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `projects`
--

INSERT INTO `projects` (`name_project`, `code`, `state`, `date_start`, `date_end`, `created_at`, `updated_at`) VALUES
('MARSELO', NULL, 'EN EJECUCION', '06/03/2020', '13/03/2020', '2020-03-06 07:55:53', '2020-03-06 07:55:53'),
('SALADITOS', 'xd123xd', 'FINALIZADO', '06/03/2020', '21/03/2020', '2020-03-06 07:59:13', '2020-03-06 07:59:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `project__invs`
--

CREATE TABLE `project__invs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `namepro` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_inv` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `project__invs`
--

INSERT INTO `project__invs` (`id`, `namepro`, `name_inv`, `created_at`, `updated_at`) VALUES
(1, 'MARSELO', 'MANUEL ALEJANDRO TRIGO MONTALBáN', '2020-03-06 07:55:54', '2020-03-06 07:55:54'),
(2, 'MARSELO', 'NAOMI ALISON ANDREA CHAVEZ OSORIO', '2020-03-06 07:55:54', '2020-03-06 07:55:54'),
(3, 'SALADITOS', 'MANUEL ALEJANDRO TRIGO MONTALBáN', '2020-03-06 07:59:13', '2020-03-06 07:59:13'),
(4, 'SALADITOS', 'CELESTE ROJELIA BLANCO NEGRETE', '2020-03-06 07:59:13', '2020-03-06 07:59:13'),
(5, 'SALADITOS', 'RODRIGO ROBERTO ROJERLIO RODRIGUEZ', '2020-03-06 07:59:13', '2020-03-06 07:59:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publications`
--

CREATE TABLE `publications` (
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title2` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `revact` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pubtype` enum('INDEXADA','NO INDEXADA') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'INDEXADA',
  `subpubtype` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `proy` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `publications`
--

INSERT INTO `publications` (`title`, `title2`, `revact`, `date`, `pubtype`, `subpubtype`, `proy`, `created_at`, `updated_at`) VALUES
('DONA GIGANTE ENCONTRADA EN MARTE', 'GIANT DONUT FOUND IN MARS', 'ELPERIODICO DE LA CIENCA FALSA', '06/03/2020', 'INDEXADA', 'WOS', 'MARSELO', '2020-03-06 10:21:12', '2020-03-06 10:21:12'),
('EL MISTERIO DETRáS DE LOS IMANES', '', 'DELICIAS', '06/03/2020', 'NO INDEXADA', 'REVISTA', 'NULL', '2020-03-06 12:26:34', '2020-03-06 12:26:34'),
('PLATILLO VOLADOR EN ANTOFAGASTA', '', 'AAA3', '06/03/2020', 'NO INDEXADA', 'CONGRESO', 'NULL', '2020-03-06 12:28:52', '2020-03-06 12:28:52'),
('VIVIMOS EN UNA SOCIEDAD', '', 'MARVEL COMICS', '14/03/2020', 'INDEXADA', 'WOS', 'MARSELO', '2020-03-06 10:01:08', '2020-03-06 10:01:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publication_invs`
--

CREATE TABLE `publication_invs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `title_inv` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nameinv` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `publication_invs`
--

INSERT INTO `publication_invs` (`id`, `title_inv`, `nameinv`, `created_at`, `updated_at`) VALUES
(1, 'VIVIMOS EN UNA SOCIEDAD', 'MANUEL ALEJANDRO TRIGO MONTALBáN', '2020-03-06 10:01:08', '2020-03-06 10:01:08'),
(2, 'VIVIMOS EN UNA SOCIEDAD', 'ANA MERCEDES MONTALBAN FLORES', '2020-03-06 10:01:08', '2020-03-06 10:01:08'),
(3, 'VIVIMOS EN UNA SOCIEDAD', 'RODRIGO ROBERTO ROJERLIO RODRIGUEZ', '2020-03-06 10:01:08', '2020-03-06 10:01:08'),
(4, 'VIVIMOS EN UNA SOCIEDAD', 'RAMON ANDRES SANCHEZ AVILA', '2020-03-06 10:01:08', '2020-03-06 10:01:08'),
(5, 'DONA GIGANTE ENCONTRADA EN MARTE', 'MANUEL ALEJANDRO TRIGO MONTALBáN', '2020-03-06 10:21:12', '2020-03-06 10:21:12'),
(6, 'DONA GIGANTE ENCONTRADA EN MARTE', 'CELESTE ROJELIA BLANCO NEGRETE', '2020-03-06 10:21:12', '2020-03-06 10:21:12'),
(7, 'DONA GIGANTE ENCONTRADA EN MARTE', 'RAMON EUGENIO DIAZ TRIGO', '2020-03-06 10:21:12', '2020-03-06 10:21:12'),
(8, 'DONA GIGANTE ENCONTRADA EN MARTE', 'MARIANO LUIS MAGANA ABRIGO', '2020-03-06 10:21:13', '2020-03-06 10:21:13'),
(9, 'DONA GIGANTE ENCONTRADA EN MARTE', 'LUIS JESUS TRIGO TABORGA', '2020-03-06 10:21:13', '2020-03-06 10:21:13'),
(10, 'EL MISTERIO DETRáS DE LOS IMANES', 'ANA MERCEDES MONTALBAN FLORES', '2020-03-06 12:26:34', '2020-03-06 12:26:34'),
(11, 'EL MISTERIO DETRáS DE LOS IMANES', 'AAA AAA AAA AAA', '2020-03-06 12:26:34', '2020-03-06 12:26:34'),
(12, 'EL MISTERIO DETRáS DE LOS IMANES', 'AAA AAAA AAAA AAAA', '2020-03-06 12:26:34', '2020-03-06 12:26:34'),
(13, 'EL MISTERIO DETRáS DE LOS IMANES', 'AAA AAA BBB AAA', '2020-03-06 12:26:34', '2020-03-06 12:26:34'),
(14, 'PLATILLO VOLADOR EN ANTOFAGASTA', 'CELESTE ROJELIA BLANCO NEGRETE', '2020-03-06 12:28:52', '2020-03-06 12:28:52'),
(15, 'PLATILLO VOLADOR EN ANTOFAGASTA', 'RODRIGO ROBERTO ROJERLIO RODRIGUEZ', '2020-03-06 12:28:52', '2020-03-06 12:28:52'),
(16, 'PLATILLO VOLADOR EN ANTOFAGASTA', 'AAA AAA AAA AA', '2020-03-06 12:28:52', '2020-03-06 12:28:52'),
(17, 'PLATILLO VOLADOR EN ANTOFAGASTA', 'AAA AAA AAA AAA', '2020-03-06 12:28:52', '2020-03-06 12:28:52'),
(18, 'PLATILLO VOLADOR EN ANTOFAGASTA', 'AAA AAA AAA AAAA', '2020-03-06 12:28:52', '2020-03-06 12:28:52');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_type` enum('ADMINISTRADOR','INVESTIGADOR') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'ADMINISTRADOR',
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name`, `user_type`, `email`, `email_verified_at`, `password`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'AdminManu', 'ADMINISTRADOR', 'admin1@admin.com', NULL, '$2y$10$ZswpcHsBkCRck4oSLI/Mr.BPPtutnvoU/VFUtEOqoKHatn01TtQv.', NULL, '2020-03-04 09:13:43', '2020-03-04 09:13:43'),
(2, 'Rebecca', 'INVESTIGADOR', 'rebecca1@gmail.com', NULL, '$2y$10$H0563bMj8gYl/XdrcRQexejWuWecgKpUzlHpJd2f3hbninaSWQ6qW', NULL, '2020-03-05 19:38:03', '2020-03-05 19:38:03'),
(10, 'Matias01', 'INVESTIGADOR', 'matiasxd@gmail.com', NULL, '$2y$10$WTL.I6MUikdlxG1LrLyE0uOY8maRZMTh/YwPuzkJ9lcZtabOJ34l2', NULL, '2020-03-06 04:56:40', '2020-03-06 04:56:40');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `country_units`
--
ALTER TABLE `country_units`
  ADD KEY `country_units_namegroup_foreign` (`namegroup`);

--
-- Indices de la tabla `groups`
--
ALTER TABLE `groups`
  ADD UNIQUE KEY `groups_name_unique` (`name`);

--
-- Indices de la tabla `investigators`
--
ALTER TABLE `investigators`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `investigators_name_unique` (`name`);

--
-- Indices de la tabla `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `password_resets`
--
ALTER TABLE `password_resets`
  ADD KEY `password_resets_email_index` (`email`);

--
-- Indices de la tabla `projects`
--
ALTER TABLE `projects`
  ADD UNIQUE KEY `projects_name_project_unique` (`name_project`);

--
-- Indices de la tabla `project__invs`
--
ALTER TABLE `project__invs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project__invs_namepro_foreign` (`namepro`);

--
-- Indices de la tabla `publications`
--
ALTER TABLE `publications`
  ADD UNIQUE KEY `publications_title_unique` (`title`);

--
-- Indices de la tabla `publication_invs`
--
ALTER TABLE `publication_invs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `publication_invs_title_inv_foreign` (`title_inv`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `investigators`
--
ALTER TABLE `investigators`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `project__invs`
--
ALTER TABLE `project__invs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `publication_invs`
--
ALTER TABLE `publication_invs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `country_units`
--
ALTER TABLE `country_units`
  ADD CONSTRAINT `country_units_namegroup_foreign` FOREIGN KEY (`namegroup`) REFERENCES `groups` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `project__invs`
--
ALTER TABLE `project__invs`
  ADD CONSTRAINT `project__invs_namepro_foreign` FOREIGN KEY (`namepro`) REFERENCES `projects` (`name_project`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `publication_invs`
--
ALTER TABLE `publication_invs`
  ADD CONSTRAINT `publication_invs_title_inv_foreign` FOREIGN KEY (`title_inv`) REFERENCES `publications` (`title`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
