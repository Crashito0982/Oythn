WITH EVT AS (
    SELECT
          DOCID
        , MAX(CASE WHEN EVTTDI = 1 THEN 1 ELSE 0 END) AS TieneEntrega
        , MAX(CASE WHEN EVTTDI IN (16,19,70) THEN 1 ELSE 0 END) AS TieneEstadoFinal
    FROM LGLIB_LGMEVT
    WHERE EVTTDI IN (1,16,19,70)          -- importante: filtrar acá
    GROUP BY DOCID
)
SELECT TOP (10)
      A.ID_LOGISTICA
    , C.DOCID
FROM CORPDW_V_R_SOL_ALTA_TC A
JOIN LGLIB_LGMDOC C
    ON C.DOCID = A.ID_LOGISTICA
JOIN ODSP_LGLIB_LGMTDC T
    ON  T.TDCPRI = C.DOCPRI
    AND T.TDCID  = C.DOCTDI
    AND (
            (T.TDCPR  = 'TARJ.C' AND T.TDCID IN (1,36,37,70,89,116,132))
         OR (T.TDCPRI = '105'    AND T.TDCID = 89)
        )
JOIN EVT E
    ON E.DOCID = A.ID_LOGISTICA
WHERE A.ID_LOGISTICA IS NOT NULL
  AND E.TieneEntrega = 1
  AND E.TieneEstadoFinal = 0
ORDER BY A.ID_LOGISTICA ASC;


##################################

USE AT_CMDTS;
GO

SELECT TOP (10)
      A.ID_LOGISTICA
    , E.DOCID
    -- , acá podés agregar más columnas que necesites, por ejemplo:
    -- , A.NRO_TARJETA
    -- , C.DOCPRI, C.DOCTDI
    -- , T.TDCPR, T.TDCID
FROM CORPDW_V_R_SOL_ALTA_TC A
JOIN LGLIB_LGMDOC C
    ON C.DOCID = A.ID_LOGISTICA
JOIN ODSP_LGLIB_LGMTDC T
    ON  T.TDCPRI = C.DOCPRI
    AND T.TDCID  = C.DOCTDI
    AND (
            (T.TDCPR  = 'TARJ.C' AND T.TDCID IN (1,36,37,70,89,116,132))
         OR (T.TDCPRI = '105'    AND T.TDCID = 89)
        )
JOIN LGLIB_LGMEVT E
    ON E.DOCID = A.ID_LOGISTICA
WHERE A.ID_LOGISTICA IS NOT NULL
  -- Evento de entrega
  AND E.EVTTDI = 1
  -- No debe existir activada / destruida / firmas varias
  AND NOT EXISTS (
        SELECT 1
        FROM LGLIB_LGMEVT E2
        WHERE E2.DOCID  = A.ID_LOGISTICA
          AND E2.EVTTDI IN (16,19,70)
  )
ORDER BY A.ID_LOGISTICA ASC;
