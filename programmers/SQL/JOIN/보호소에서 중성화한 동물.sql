SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS O
JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.SEX_UPON_OUTCOME != I.SEX_UPON_INTAKE
ORDER BY O.ANIMAL_ID
