def Messages():
    """create dictionary of Spanish messages"""
    m = {}
    m['AddCompoundError']       = "Proveedor de termodin�mica repora el siguiente error al agregar el compuesto:\n%s"
    m['AdjustingFromOlderVersion'] = "Caso cargado fue creado en una versi�n anterior. Actualizando de: Diagrama de flujo versi�n = %d; ReleaseVersion = %s. A: Diagrama de flujo versi�n %d; ReleaseVersion %s"
    m['AfterPortDisconnect']    = "%s desconectado de %s"
    m['BalanceInvalidPort']    = "Puerto no v�lido para balance(no materia o energ�a)"
    m['BeforePortDisconnect']   = "Desconectando %s de %s"
    m['BubbleTCouldNotCalc']    = "La Temperatura de Punto de Burbuja no se pudo calcular en %s a P = %s kPa y composici�n = %s"
    m['CalcDisturbance']        = "Calculando perturbaci�n %i de %i en jacobiano de %s"
    m['CantAddObject']         = "No se puede agregar %s a %s"
    m['CantAddToStage']        = "No se puede agregar %s a la etapa %d de %s"
    m['CantAddToStageObject']  = "No se puede agregar %s a %s en la etapa %d de %s"
    m['CantChangeName']         = "No se puede cambiar el nombre de %s"
    m['CantCreateSpec']         = "No se puede crear Spec %s. Probablemente no est� soportado"
    m['CantDeleteFromStage']   = "No se puede borrar %s de la etapa %d de %s"
    m['CantDeleteObject']      = "No se puede borrar objeto %s. Operaci�n unitaria no puede resolver sin �l"
    m['CantFindPhCh']           = "No se pueden encontrar cambios de fase en %s para m�s de dos lados o cuando se resuelve en rating mode (valores de UA especificados)"
    m['CantMoveToStage']        = "No se puede mover %s a la etapa %d de %s. Aseg�rese que no hay un conflicto con los nombres"
    m['CantOverwriteThermo']   = "No se puede sobreescribir un caso termodin�mico. El procedimiento correcto es borrar el caso anterior primero y despu�s establecer uno nuevo. Operaci�n unitaria: %s; Termodin�mica actual: %s"
    m['CantSetIP']              = "No se puede establecer el par�metro de interacci�n  con el valor %f para los compuestos %s y %s"
    m['CantSetLiqPhPar']       = "El n�mero de fases l�quidas no puede ser %s"
    m['CantSetSingleFrac']      = "No se puede establecer la fracci�n masa o volumen de un solo compuesto %s en el puerto de materia %s."
    m['CantSetParameter']       = "no se puede asignar al par�metro %s el valor %s"
    m['ChangedEffMatrix']       = "La Matriz de Eficiencias cambi�n como resultado de un cambio en la configuraci�n de %s"
    m['CompNotNormalized']      = "La suma de las fracciones mol de %s es %f, no 1"
    m['ConnectErrorNoPort']     = "No se puede conectar %s.%s a %s.%s por que falta un puerto"
    m['ConnectErrorNoUop']      = "No se puede conectar %s.%s a %s.%s por que falta una op unit"
    m['ConnectSameTypePorts']  = "Intento de conectar puertos de diferentes tipos en %s"
    m['ConnectSigToNonSig']     = "Intento de conectar puerto de se�al %s a un puerto que no es de se�al"
    m['ContDerivCalc']          = "Controlador de solver para %s calculando derivada %d"
    m['ControllerConvergeFail'] = "Controlador de solver para %s fall� para convergir"
    m['ControllerTotalError']   = "Controlador de solver para %s error - %f"
    m['Converged']              = "%s convirgi� en %i iteraciones"
    m['CouldNotConverge']       = "No se pudo resolver %s despu�s de %d iteraciones"
    m['CouldNotConvergeInner']  = "No se pudo resolver el Ciclo Interno %s despu�s de %d iteraciones"
    m['CouldNotConvergeOuter']  = "No se pudo resolver el Ciclo Externo %s despu�s de %d iteraciones"
    m['CouldNotConvergeUA']     = "No se pudo resolver para UA = %f en %s"
    m['CouldNotInitialize']     = "No se pudo inicializar el set de ecuaciones al intentar resolver %s"
    m['CouldNotInvertJacobian'] = "No se pudo invertir el Jacobiano en %s"
    m['CouldNotLoadLanguage']   = "No se pudo cargar lenguage %s"
    m['CouldNotLoadProvider']   = "No se pudo cargar proveedor de termodin�mica  %s"
    m['CouldNotSolve']          = "No se pudo resolver %s"
    m['CouldNotSolveNonSuppFlash'] = "No se pudo resolver flash no soportado %s = %s, %s = %s in %s"
    m['CreatePortTypeError']    = "Puerto %s no tiene un tipo v�lido en %s"
    m['CrossConnMoleLoss']      = "Una p�rdida significativa de flujo molar de %f fue detectada en el Cross Connector %s. Una raz�n com�n es la diferencia de compuestos que contienen flujos significativos"
    m['DeletePortError']        = "No se puede borrar puerto %s de %s"
    m['DewTCouldNotCalc']       = "La Temperatura de Punto de Roc�o no pudo ser calculada en %s a P = %s kPa y composici�n = %s"
    m['DiffThCaseInConn']       = "Casos termodin�micos diferentes encontrados en la conexi�n de puertos %s -> %s. No se pudo pasar el valor"
    m['DuplicateName']          = "El Comando fall� debido al nombre dupllicado de %s en %s"
    m['ErrInCleanUp']           = "Error al limpiar %s"
    m['ErrNotifyChangeCmp']     = "Error al notificar a %s de un cambio en la lista de compuestos"
    m['ErrNotifyLiqChange']     = "Error al notificar a %s de un cambio en el n�mero de fases l�quidas. LiquidPhases = %s"
    m['ErrNotifyParChange']     = "Error al notificar a %s de un cambio en el valor de un par�metro. %s = %s"
    m['ErrNotifySolChange']     = "Error al notificar a %s de un cambio en el n�mero de fases s�lidas. LiquidPhases = %s"
    m['ErrNotifyThChange']      = "Error al notificar a %s de un cambio en el caso termodin�mico. ThermoCase = %s"
    m['ERRSettingThermo']     = "Error al intentar establecer termodin�mica en la operaci�n unitaria: %s; Termodin�mica intentada: %s"
    m['ErrorSolvingDesign']     = "Error al resolver objeto de dise�o %s"
    m['ERRTowerArithmetic']     = "Torre %s no puede convergir debido a un error aritm�tico"
    m['EqnBasedUOpError']        = "%s iteraci�n %d m�ximo error %f"
    m['EqnCalcError']           = "Error de c�lculo en %s"
    m['EqnDuplicateSigName']    = "Nombre de se�al %s es usado m�s de una vez en la ecuaci�n %s"
    m['EqnNumbMismatch']       = "Error contando las ecuaciones en %s"
    m['EqnParenMismatch']       = "Discrepancia en par�ntesis en %s de la ecuaci�n %s"
    m['EqnSyntax']              = "Error de sintaxis %s en la ecuaci�n %s"
    m['EqnUnknownToken']        = "No se sabe como manejar %s en la ecuaci�n %s de %s"
    m['HotTLowerThanColdT']     = "La temperatura de entrada de la corriente caliente %f es menor que la de la corriente fria %f en %s"
    m['HydrateCouldNotCalc']  = "La temperatura del hidrato no se pudo calcular en %s a P = %s kPa y composici�n = %s"
    m['HydrateLowP']            = "Hidrato no se puede formar a la baja presi�n de P = %s kPa en %s"
    m['InvalidCalcStatusInSet'] = "calcStatus no v�lido en SetValue"
    m['InvalidComposition']     = "La composici�n %s = %f en %s.  Ha sido igualada a cero."
    m['InvalidDrawPhase']      = "Fase no v�lida para la salida en la etapa %d de %s"
    m['InvalidTowerSpecPhase'] = "Fase no v�lida en la espec en la etapa %d de %s"
    m['LumpLiqs']               = "Un segundo l�quido con fracci�n %f es detectado en flash VL."
    m['MaxSolverIterExceeded']  = "M�ximo %d iteraciones excedido resolviendo la hoja de flujo %s"
    m['MissigZInCommonProps']   = "El Factor Z debe estar siempre en las propiedades comunes. Se intent� establecer: %s"
    m['NonHydrateFormerFound']  = "No se encontr� ning�n compuesto formador de hidratos en %s"
    m['NoPkgSelected']          = "No se seleccion� un paquete termodin�mico cuando se intent� crear %s"
    m['NoPortDirection']        = "Puerto %s requiere direcci�n (in o out) en %s"
    m['NoSupportForReqArrProps']= "El proveedor de termodin�mica %s no soporta las siguientes propiedades requeridas %s"    
    m['NoSupportForReqProps']   = "El proveedor de termodin�mica %s no soporta las siguientes propiedades requeridas %s"
    m['NotConverging']          = "%s parece no convergir y los c�lculos se detuvieron. Cambie el par�metro MonitorConvergence a 0 si desea desactivar esta opci�n"
    m['NoVersionUpdate']        = "No actualizaci�n para %d (%s) para %d (%s)"
    m['PortNotFlashedDesignObj']= "Los puertos de la operaci�n unitaria no est�n flasheados, por lo tanto, el objeto de dise�o %s no est� listo para ser resuelto"
    m['RawOutput']             = "%s"
    m['RecycleErrorDetail']     = "%s %s %g vs %g"
    m['RecycleConsistency']     = "Error de consistencia %s %s %g vs %g"
    m['RecycleIter']            = "Iteraci�n %d -> max Error %f"
    m['RenamePortError']        = "No se puede renombrar el puerto %s a %s"
    m['RenamePortNameExists']   = "No se puede renombrar el puerto %s a %s debido a que ese nombre ya est� en uso"
    m['RevertingFromNewerVersion'] = "Caso cargado creado en versi�n m�s nueva. Actualizando de: diagrama de flujo versi�n %d, versi�n oficial %s. A: diagrama de flujo versi�n %d versi�n oficial %s"
    m['SetValueUnknownNotNone'] = "SetValue con la bandera UNKNOWN_V debe tener valor = None"
    m['SetVarTypeMismatch']     = "Tipo de variable de puerto %s no es %s en %s"
    m['SigConnectTypeMismatch'] = "Conflicto en tipo de variable (%s vs %s) conectando %s a %s"
    m['SigShareMismatch']       = "Conflicto en tipo de variable (%s vs %s) compartiendo %s con %s"
    m['SolvingDesign']          = "Resolviendo objeto de dise�o %s"
    m['SolvingOp']              = "Resolviendo operaci�n %s"
    m['TemperatureCross']       = "Cruce de temperatura (%f %f) en %s"
    m['TooManySolidPhases']     = "Demasiadas fases s�lidas requeridas(%d) cuando se intent� flashear desde %s"
    m['TooManyTowerSpecs']     = "%d especs encontradas, solo %d es necesaria en %s"
    m['TowerCalcJacobian']      = "Calculando jacobiano para %s"
    m['TowerCmpMatrixError']    = "%s tuvo un error al resolver los balances de materia para el compuesto %d"
    m['TowerDeletePort']        = "No se puede borrar directamente el puerto %s de %s"
    m['TowerEffSetToOne']       = "La eficiencia de la etapa superior de la Torre fue especificada como 1.0 porque la salida de vapor es 0"
    m['TowerFailedToConverge']  = "%s fall� para convergir %d iteraciones - error = %f"
    m['TowerInnerError']        = "%s Error interno %f"
    m['TowerNoPressure']        = "Presiones de salida no disponibles para la torre %s"
    m['TowerOuterError']        = "%s iteraci�n %d error externo %f"
    m['TowerQSpecError']       = "No se puede asignar flujo de energ�a a la etapa %d"
    m['TowerRemoveLastStage']   = "No se puede remover %d etapas debajo de la etapa %d"
    m['TowerPARemovalError']    = "No se puede remover una etapa con una alimentaci�n a Pump around a menos que el Pump around sea removido tambi�n. La alimentaci�n est� en la etapa %i, pump around desde la etapa %i"
    m['TowerSSRemoveError']     = "Etapas superior o inferior de la torre no pueden ser removidas a menos que se remueva toda la secci�n"
    m['TowerUpdateEffErr']      = "Ocurri� un error al intentar la actualizaci�n de la matriz de eficiencias en %s. Por favor actualice manualmente"
    m['UpdateInvalidPort']      = "Puerto %s no existe en %s - no se puede actualizar"
    m['WrongDiamEjector']       = "Especificaci�n incorrecta de di�metro en %s. Di�metro del Nozzle debe ser menor al di�metro del throat. Nozzle D = %f; Throat D = %f"
    m['WrongNumberTowerSpecs'] = "Discrepancia en el n�mero de especs de la torre - %d vs %d necesarias en %s"
    m['WrongParentDesignObj']   = "Objeto de dise�o %s contenido en el tipo incorrecto de operaci�n unitaria"
    m['DoneSolving']            = "Hoja de flujo %s resuelta"
    m['NoMessage']              = ""
    m['MissingValue']           = "%s no tiene valor"
    m['ErrorValue']             = "Error = %s"
    m['OK']                     = "OK"

    #Properties are grouped together
    m['T']                      = "Temperatura"
    m['P']                      = "Presi�n"
    m['H']                      = "Entalp�a"
    m['VapFrac']                = "Fracci�nVapor"
    m['MoleFlow']               = "FlujoMolar"
    m['MassFlow']               = "FlujoMasa"    
    m['VolumeFlow']             = "FlujoVol"  
    m['Energy']                 = "FlujoEnerg�a"
    m['MolecularWeight']        = "PesoMolecular"  
    m['ZFactor']                = "FactorZ"
    return m

