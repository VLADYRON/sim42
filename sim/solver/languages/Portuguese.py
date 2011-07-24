# Contributed by J.-Henrique Pinto  2004-Feb-15
#Contribui��o de Jos�-Henrique Pinto. 2004-Feb-15

def Messages():
    """create dictionary of English messages :: mensagens em portugu�s"""
    m = {}
    m['AddCompoundError']            = "Provedor de propriedades f�sicas indica o seguinte erro ao adicionar o composto:\n%s"
    m['AdjustingFromOlderVersion']   = "Abertura de um caso criado em uma antiga vers�o. Atualiza��o a partir de: FlowsheetVersion = %d; Vers�o = %s. A: FlowsheetVersion %d; vers�o %s"
    m['AfterPortDisconnect']         = "% desconectado de %s"
    m['BalanceInvalidPort']          = "Porta n�o � v�lida para o balan�o: n�o � massa ou energia"
    m['BeforePortDisconnect']        = "Desconex�o de %s de %"
    m['BubbleTCouldNotCalc']         = "N�o foi poss�vel calcular a temperatura de ponto de bolha em %s com P = %s kPa e composi��o = %s"
    m['CalcDisturbance']             = "C�lculo da perturba��o %i de %i no jacobiano de %s"
    m['CalculatingStep']             = "C�lculo do passo %i em %s. Atualmente em %g. Indo de %g a %g"
    m['CantAddObject']               = "Imposs�vel incluir %s em %s"
    m['CantAddToStage']              = "Imposs�vel incluir %s ao est�gio %d de %s"
    m['CantAddToStageObject']        = "Imposs�vel incluir %s em %s no est�gio %d de %s"
    m['CantChangeName']              = "Imposs�vel modificar o nome de %s"
    m['CantCreateSpec']              = "Imposs�vel criar especif. %s. Provavelmente esta n�o � compat�vel"
    m['CantDeleteFromStage']         = "Imposs�vel excluir %s no est�gio %d de %s"
    m['CantDeleteObject']            = "Imposs�vel excluir o objeto %s. O c�lculo da op. unit. n�o � poss�vel sem o mesmo"
    m['CantDelPortDirectly']         = "Imposs�vel excluir a porta %s de %s. Exclua o objeto associado"
    m['CantFindPhCh']                = "Imposs�vel encontrar mudan�as de fase em %s para mais de dois lados ou durante a solu��o em modo de avalia��o (valores UA especificados)"
    m['CantMoveToStage']             = "Imposs�vel mover %s ao est�gio %d de %s. Verifique se h� algum conflito nos nomes"
    m['CantOverwriteThermo']         = "Imposs�vel substituir um caso de termodin�mica por outro. Primeiro exclua o antigo caso de termodin�mica e depois crie um novo. Op. unit.: %s; caso termodin. em uso: %s"
    m['CantSetIP']                   = "Imposs�vel estabelecer um par�metro interativo de valor igual a %f para os compostos %s e %s"
    m['CantSetLiqPhPar']             = "Imposs�vel estabelecer o n�mero de fases l�quidas como %s"
    m['CantSetSingleFrac']           = "Imposs�vel definir a fra��o m�ssica ou volum�trica de somente um componente %s na porta de mat�ria %s."
    m['CantSetParameter']            = "Imposs�vel atribuir o valor %s ao par�metro %s"
    m['ChangedEffMatrix']            = "Houve mudan�a na matriz de efici�ncias como conseq��ncia de uma altera��o da configura��o em %s"
    m['CompNotNormalized']           = "A soma das fra��es molares de %s � %f e n�o 1"
    m['ConnectErrorNoPort']          = "Imposs�vel conectar %s.%s a %s.%s pois falta uma porta"
    m['ConnectErrorNoUop']           = "Imposs�vel conectar %s.%s a %s.%s pois falta uma op. unit�ria"
    m['ConnectSameTypePorts']        = "Tentativa de conex�o de portas de tipos diferentes em %s"
    m['ConnectSigToNonSig']          = "Tentativa de conex�o de porta de sinal %s a uma porta de tipo diferente"
    m['ContDerivCalc']               = "C�lculo de derivadas %d pelo calculador do controlador de %s"
    m['ControllerConverge Fail']     = "O calculador do controlador de %s n�o convergiu"
    m['ControllerTotalError']        = "Erro no calculador do controlador de %s - %f"
    m['Converged']                   = "Converg�ncia de %s atingida em %i itera��es"
    m['CouldNotConverge']            = "Imposs�vel convergir %s ap�s %d itera��es"
    m['CouldNotConvergeInner']       = "Imposs�vel convergir as repeti��es internas %s ap�s %d itera��es"
    m['CouldNotConvergeOuter']       = "Imposs�vel convergir as repeti��es externas %s ap�s %d itera��es"
    m['CouldNotConvergeUA']          = "Imposs�vel calcular para UA = %f em %s"
    m['CouldNotInitialize']          = "Imposs�vel inicializar o conjunto de equa��es durante o c�lculo %s"
    m['CouldNotInvertJacobian']      = "Imposs�vel inverter o Jacobiano em %s"
    m['CouldNotLoadLanguage']        = "Imposs�vel obter o idioma %s"
    m['CouldNotLoadProvider']        = "Imposs�vel obter o pacote termodin. %s"
    m['CouldNotRestorePlugIn']       = "Imposs�vel restaurar o objeto `plugin� %s ao retomar o caso. O objeto predeterminado ser� utilizado"
    m['CouldNotSolve']               = "Imposs�vel calcular %s"
    m['CouldNotSolveNonSuppFlash']   = "Imposs�vel calcular flash com as vari�veis %s = %s, %s = %s em %s"
    m['CreatePortTypeError']         = "O tipo da porta %s n�o est� correto em %s"
    m['CrossConnMoleLoss']           = "Uma perda sens�vel da vaz�o molar de %f foi detectada no conector cruzado %s. Uma poss�vel raz�o � a discrep�ncia entre os compostos que apresentam fluxos importantes"
    m['DeletePortError']             = "Imposs�vel excluir a porta %s de %s"
    m['DewTCouldNotCalc']            = "N�o foi poss�vel calcular a temperatura de ponto de orvalho em %s com P = %s kPa e composi��o = %s"
    m['DiffThCaseInConn']            = "Caso termodin. diferente encontrado na conex�o de porta %s -> %s. N�o foi poss�vel transferir os valores"
    m['DuplicateName']               = "Falha na execu��o do comando devida a uma duplica��o do nome %s em %s"
    m['ErrInCleanUp']                = "Erro ao consolidar os dados de %s"
    m['ErrNotifyChangeCmp']          = "Erro ao notificar %s sobre uma altera��o na lista de componentes"
    m['ErrNotifyLiqChange']          = "Erro ao notificar %s sobre uma altera��o no no de fases l�quidas. FasesL�quidas = %s"
    m['ErrNotifyParChange']          = "Erro ao notificar %s sobre uma altera��o no valor de um par�metro. %s = %s"
    m['ErrNotifySolChange']          = "Erro ao notificar %s sobre uma altera��o no no de fases s�lidas. FasesL�quidas = %s"
    m['ErrNotifyThChange']           = "Erro ao notificar %s sobre uma altera��o do caso termodin. CasoTermodin = %s"
    m['ERRSettingThermo']            = "Erro durante a tentativa de configura��o de termodin. na op.unit.: %s; Termodin. tentada: %s"
    m['ErrSpecialProp']              = "Erro ao calcular a propriedade especial em %s. Mensagem do fornecedor de dados termodin�micos: %s"
    m['ErrorSolvingDesign']          = "Erro durante o c�lculo do objeto %s"
    m['ERRTowerArithmetic']          = "A coluna %s n�o convergiu devido a um erro aritm�tico"
    m['EqnCalcError']                = "Erro no c�lculo de %s"
    m['EqnDuplicateSigName']         = "O nome do sinal %s foi usado mais de uma vez na equa��o %s"
    m['EqnNumbMismatch']             = "Erro na contagem de equa��es em %s"
    m['EqnParenMismatch']            = "Discrep�ncia no no de par�nteses em %s da equa��o %s"
    m['EqnSyntax']                   = "Erro de sintaxe em %s na equa��o %s"
    m['EqnUnknownToken']             = "Erro no s�mbolo %s na equa��o %s de %s"
    m['EqnBasedUOpError']            = "%s Itera��o %d erro m�x. %f"
    m['HotTLowerThanColdT']          = "A temperatura da entrada quente %f � inferior � da entrada fria %f em %s"
    m['HydrateCouldNotCalc']         = "A temperatura do hidrato n�o p�de ser calculada em %s a P = %s kPa e composi��o = %s"
    m['HydrateLowP']                 = "Hidrato n�o pode ser formado sob condi��o de baixa press�o de P = %s kPa em %s"
    m['InnerErrorDetail']            = "%s detalhes interiores. Erro: %13.6g ; MaxErrorValue: %13.6g ; MaxErrorEqnName: %s"
    m['InnerLoopSummary']            = """%s Resumo do anel interior:
        MaxErrorEqnName:......... %s
        MaxErrorValue:........... %.6g
        
        MaxDeltaTStage(0 at top): %i
        MaxDeltaTValue(New-Old):. %0.4g
        
        Converg�ncia:............... %i
        Itera��es:.............. %i"""
    m['InvalidCalcStatusInSet']      = "calcStatus n�o � v�lido em SetValue"
    m['InvalidComposition']          = "A composi��o %s = %f na %s.  Atribu�do valor zero."
    m['InvalidDrawPhase']            = "Fase n�o � v�lida para a sa�da do est�gio %d da %s"
    m['InvalidTowerSpecPhase']       = "Fase n�o � v�lida na especifica��o do est�gio %d da %s"
    m['LumpLiqs']                    = "Uma segunda fase l�quida %f foi detectada no flash VL."
    m['MaxSolverIterExceeded']       = "M�ximo %d de itera��es excedido na resolu��o da simula��o do processo %s"
    m['MissigZInCommonProps']        = "O fator Z deve sempre estar nas propriedades comuns. Tentativa de estabelecer: %s"
    m['NonHydrateFormerFound']       = "Forma��o de um n�o hidrato encontrada vindo a %s"
    m['NoPortDirection']             = "Indicar o sentido na porta %s em %s: in (para dentro) ou out (para fora)"
    m['NoSupportForReqArrProps']     = "O provedor de termodin�mica %s n�o fornece as seguintes propriedades requeridas %s"
    m['NoSupportForReqProps']        = "O provedor de termodin�mica %s n�o fornece as seguintes propriedades requeridas %s"
    m['NotConverging']               = "Aparentemente %s n�o est� convergindo e os c�lculos foram interrompidos. Altere o valor do par�metro MonitorConvergence para 0 caso queira desativar esta funcionalidade"
    m['NoVersionUpdate']             = "Atualiza��o de %d (%s) n�o dispon�vel para %d (%s)"
    m['ODEMaxSteps']                 = "N�mero m�x. de passos de integra��o (%i) atingido em %s. Incremente ODEMaxSteps se a integra��o transcorria corretamente"
    m['OuterErrorDetail']            = "%s Itera��o %d Erro ext. %13.6g. MaxErrorStage(0 at top) %i WaterDrawError %13.6g"
    m['OverspecFlash']               = "Imposs�vel calcular o flash em %s porque h� especifica��es em excesso. Somente duas vari�veis s�o necess�rias e %i foram digitadas (%s)"
    m['PortNotFlashedDesignObj']     = "N�o foi calculado o flash das portas das op. unit. de modo que o objeto %s n�o se encontra pronto para ser calculado"
    m['RawOutput']           = "%s"
    m['RecycleErrorDetail']          = "%s %s %g contra %g"
    m['RecycleConsistency']          = "Erro de coer�ncia %s %s %g contra %g"
    m['RecycleIter']                 = "Itera��o %d -> erro m�ximo %f"
    m['RenamePort']                  = "Alterar o nome da porta  %s.%s para %s.  Ela est� conectada a %s"
    m['RenamePortError']             = "N�o se pode nomear novamente a porta %s a %s"
    m['RenamePortNameExists']        = "N�o se pode nomear novamente a porta %s a %s pois este nome se encontra em uso"
    m['RevertingFromNewerVersion']   = "Abertura de um caso criado com uma vers�o mais recente. Atualiza��o a partir de: vers�o do diagrama de processo %d, vers�o %s. A: vers�o do diagrama de processo %d vers�o %s"
    m['SetValueUnknownNotNone']      = "SetValue com um indicador UNKNOWN_V deve ter o valor = None"
    m['SetVarTypeMismatch']          = "Tipo da vari�vel da porta %s n�o � %s em %s"
    m['SigConnectTypeMismatch']      = "Conflito no tipo de vari�vel (%s contra %s) ao conectar %s a %s"
    m['SigConnectTypeMismatch']      = "Conflito no tipo de vari�vel (%s contra %s) ao compartilhar %s com %s"
    m['SolvingDesign']               = "C�lculo do objeto %s"
    m['SolvingOp']                   = "C�lculo da opera��o %s"
    m['StepSizeTooSmall']            = "Estouro aritm�tico negativo do tamanho do incremento em %s. Tamanho do incremento = %g"
    m['TemperatureCross']            = "Temperaturas cruzadas (%f %f) em %s"
    m['InternalTCross']              = "Temperaturas cruzadas em %s. Verificar os perfis para detalhes"
    m['NoPkgSelected']               = "N�o houve sele��o de um conj. termodin. durante a tentativa de cria��o de %s"
    m['ThermoProviderMsg']           = "Mensagem do fornecedor de dados termodin�micos durante a solu��o %s:\n%s"
    m['TooManySolidPhases']          = "Solicita��o de um no muito alto de fases s�lidas (%d) ao se tentar realizar o flash de %s"
    m['TooManyTowerSpecs']           = "%d especifica��es encontradas, apenas %d s�o necess�rias em %s"
    m['TowerCalcJacobian']           = "C�lculo do jacobiano para %s"
    m['TowerCmpMatrixError']         = "%s apresentou um erro no c�lculo do balan�o de massa para o componente %d"
    m['TowerDeletePort']             = "N�o se pode excluir diretamente a porta %s de %s. Selecione e exclua a especif. ou retirada correspondente"
    m['TowerEffSetToOne']            = "A efici�ncia da coluna no est�gio do topo foi definida como 1,0 porque a retirada de vapor � nula"
    m['TowerFailedToConverge']       = "%s n�o convergiu em %d itera��es - erro = %f"
    m['TowerInnerError']             = "%s Erro interno %f"
    m['TowerNoPressure']             = "N�o h� press�es de sa�da para a coluna %s"
    m['TowerOuterError']             = "%s itera��o %d erro externo %f"
    m['TowerQSpecError']             = "N�o se pode especificar carga t�rmica no est�gio %d"
    m['TowerRemoveLastStage']        = "N�o se pode excluir %d est�gios abaixo do est�gio %d"
    m['TowerPARemovalError']         = "Imposs�vel excluir um est�gio com alimenta��o fornecida por uma recircula��o de l�quido a menos que esta �ltima seja tamb�m exclu�da. A alimenta��o est� no est�gio %i e a recircula��o de l�quido prov�m do est�gio %i"
    m['TowerSSRemoveError']          = "N�o se pode excluir est�gios no topo ou no fundo da torre, a menos que toda a se��o seja exclu�da"
    m['TowerUpdateEffErr']           = "Houve um erro ao se tentar atualizar a matriz de efici�ncias em %s. Atualize manualmente."
    m['TwrNoFeed']                   = "Nenhuma alimenta��o encontrada em %s"
    m['TwrSpecErr']                  = "Error no c�lculo da especifica��o %s"
    m['TwrSpecErrConfig']            = "A especif. %s foi associada a um objeto incorreto %s. Por exemplo, uma especif. de recircula��o localizada associada a um equipamento difrenete de uma recircula��o localizada"
    m['TwrSubCooledVapDraw']         = "N�o houve converg�ncia da coluna devido a uma solu��o de subresfriamento no topo, onde h� uma retirada de vapor. Graus de subresfriamento = %f"
    m['UnresolvedConsistencyErrors'] = "Os seguintes erros de coer�ncia no processo %s n�o foram calculados (somente um erro mostrado por op. unit�ria):\n%s"
    m['UnresolvedRecycles']          = "As seguintes portas de reciclagem no processo %s n�o foram calculadas (somente uma mostrada por op. unit�ria):\n%s"
    m['UpdateInvalidPort']           = "Porta %s n�o existe %s - n�o � poss�vel atualizar"
    m['WrongDiamEjector']            = "Erro na especifica��o do di�metro em %s. O di�metro do bocal ejetor deve ser inferior ao da garganta. Di�m. ejetor = %f; di�m. garganta = %f"
    m['WrongNumberTowerSpecs']       = "Erro no n�mero de especifica��es para a coluna - %d contra %d necess�rias na %s"
    m['WrongParentDesignObj']        = "O objeto %s est� em um tipo incorreto de op. unit."
    m['WrongSetting']                = "Valor incorreto %s para definir %s no objeto %s"
    m['DoneSolving']                 = "Processo %s calculado"
    m['NoMessage']           = ""
    m['MissingValue']                = "%s n�o tem um valor"
    m['ErrorValue']                  = "Erro = %s"
    m['OK']                  = "OK"

    #Following messages not in alphabetical order to keep all the properties together
    m['T']                   = "Temperatura"
    m['P']                   = "Press�o"
    m['H']                   = "Entalpia"
    m['VapFrac']             = "Fra�. vapor"
    m['MoleFlow']            = "Vaz�o molar"
    m['MassFlow']            = "Vaz�o m�ssica"
    m['VolumeFlow']          = "Vaz�o volum."
    m['Energy']              = "Energia"
    m['MolecularWeight']     = "Massa molar"
    m['ZFactor']             = "Fator Z"
    return m

