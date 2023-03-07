/*SQL snips for def queries in GIS*/



--Purpose: Return data in interval of 5
--Use Case: Helpful for contour lines or labels
MOD(CVALUE,5) = 0



--Purpose: Determine IDs / Record #s in one table but not in other
--Use Case: Useful for seeing which data has been filtered out of joined tables

SELECT Location_ID, Location_Name
FROM WAECY_GroundwaterLevels

WHERE Location_ID NOT IN (SELECT Location_ID FROM WAECY_GWLevels_Joined_LocationInfo)