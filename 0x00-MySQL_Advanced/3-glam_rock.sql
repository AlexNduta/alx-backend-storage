-- list all bands with Glam Rock as their main style ranked by their longevity
SELECT band_name, split, formed (formed - split) as lifespan
FROM metal_bands
WHERE style = Glam rock
GROUP BY band_name
ORDER BY lifespan DESC;
