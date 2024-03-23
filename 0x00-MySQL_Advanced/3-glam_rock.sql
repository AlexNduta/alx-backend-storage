-- list all bands with Glam Rock as their main style ranked by their longevity
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style = "%Glam rock%"
ORDER BY lifespan DESC;
