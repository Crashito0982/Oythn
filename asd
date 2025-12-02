USE AT_CMDTS;
GO

IF OBJECT_ID('dbo.TC_TarjetasPendientes', 'U') IS NOT NULL
    DROP TABLE dbo.TC_TarjetasPendientes;
GO

CREATE TABLE dbo.TC_TarjetasPendientes (
    ID_LOGISTICA             BIGINT        NOT NULL,   -- usar el mismo tipo que en CORPDW_V_R_SOL_ALTA_TC
    FECHA_INGRESO_SOLICITUD DATE          NULL,        -- DATE si en SOL_ALTA_TC también es DATE
    NUMERO_CLIENTE          BIGINT        NULL,        -- ajustá al tipo real (BIGINT/INT/NUMERIC)
    NUMERO_DOCUMENTO        VARCHAR(50)   NULL,        -- ajustá el tamaño según SOL_ALTA_TC
    SITUACION_TC            VARCHAR(50)   NULL,
    ESTADO_ACTIVACION       VARCHAR(50)   NULL,
    TIPO_TARJETA_DESC       VARCHAR(100)  NULL,
    FechaDesde              DATE          NOT NULL,    -- rango calculado en el SP
    FechaEjecucion          DATETIME2(0)  NOT NULL,    -- momento de ejecución del SP
    CONSTRAINT PK_TC_TarjetasPendientes
        PRIMARY KEY CLUSTERED (ID_LOGISTICA)
);
GO
