MODULE Module1

    CONST robtarget Balde_3:=[[70,0,0],[1,0,0,0],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Balde_2:=[[0,0,0],[1,0,0,0],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Balde_1:=[[0,0,-70],[1,0,0,0],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Medio_1:=[[0,0,-70],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Medio_2:=[[0,0,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Medio_3:=[[70,0,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Home_Est:=[[300,-50,-200],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est1_2:=[[70,0,0],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est1:=[[0,0,0],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est2_2:=[[70,-250,0],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est2:=[[0,-250,0],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est3_2:=[[70,0,140],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est3:=[[0,0,140],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est4_2:=[[70,-250,140],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est4:=[[0,-250,140],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est5_2:=[[70,0,290],[1,0,0,0],[0,0,1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est5:=[[0,0,290],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est6_2:=[[70,-250,290],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est6:=[[0,-250,290],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Mid_State:=[[150,0,-250],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Balde_State:=[[200,100,-200],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est1_3:=[[0,0,20],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est2_3:=[[0,-250,20],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est3_3:=[[0,0,160],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est4_3:=[[0,-250,160],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est5_3:=[[0,0,310],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Est6_3:=[[0,-250,310],[1,0,0,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Soltar_State:=[[150,0,-250],[0.707106781,0,0.707106781,0],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Soltar_2:=[[-10,0,-70],[0.707106781,0,0.707106781,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Soltar_1:=[[-10,0,0],[0.707106781,0,0.707106781,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Medio_4:=[[-50,0,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
!***********************************************************
    !
    ! Module:  Module1
    !
    ! Description:
    !   <Proyecto>
    !
    ! Author: Cristhian Sandoval, Juan Pablo Vallejo, Dylan Ortiz
    !
    ! Version: 1.0
    !
    !***********************************************************
    
    
    !***********************************************************
    !
    ! Procedure main
    !
    !   This is the entry point of your program
    !
    !***********************************************************
    PROC main()
       
        Balde_Tomar;
        Medio_Dejar;
        WaitTime(3);
        Medio_Dejar2;
        WaitTime(3);
        IF DI_01=1 THEN
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_1;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_2;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_4;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_6;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
        ELSEIF DI_02=1 THEN
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_5;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_1;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_4;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_2;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
        ELSEIF DI_03=1 THEN
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_6;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_4;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_2;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_1;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
        ELSEIF DI_04=1 THEN
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_3;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_4;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_2;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
            
            WaitTime(1);
            SetDO DO_02,1;
            WaitTime(1);
            SetDO DO_02,0;
            Toma_1;
            Soltar_Ficha;
            WaitTime(1);
            SetDO DO_01,1;
            WaitTime(1);
            SetDO DO_01,0;
            Soltar_Volver;
        ENDIF
        Medio_Tomar;
        Balde_Dejar;
 
    ENDPROC
    

    PROC Toma_1()
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
        MoveL Est1_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est1,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est1_3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est1,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est1_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
    ENDPROC
    PROC Toma_2()
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
        MoveL Est2_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est2_3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est2_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
    ENDPROC
    PROC Toma_3()
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
        MoveL Est3_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est3_3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est3_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Home_Est,v500,z100,ventosa\WObj:=Estanteria;
    ENDPROC
    PROC Toma_4()
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
        MoveL Est4_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est4,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est4_3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est4,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est4_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Home_Est,v500,z100,ventosa\WObj:=Estanteria;
    ENDPROC
    PROC Toma_5()
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
        MoveL Est5_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est5,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est5_3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est5,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est5_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Home_Est,v500,z100,ventosa\WObj:=Estanteria;
    ENDPROC
    PROC Toma_6()
        MoveJ Home_Est,v500,z50,ventosa\WObj:=Estanteria;
        MoveL Est6_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est6,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est6_3,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est6,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Est6_2,v200,z100,ventosa\WObj:=Estanteria;
        MoveL Home_Est,v500,z100,ventosa\WObj:=Estanteria;
    ENDPROC
    PROC Balde_Tomar()
        MoveJ Valde_State,v600,z100,gancho\WObj:=Vald;
        MoveL Valde_3,v200,z100,gancho\WObj:=Vald;
        MoveL Valde_2,v200,z100,gancho\WObj:=Vald;
        MoveL Valde_1,v100,z100,gancho\WObj:=Vald;
        MoveJ Valde_State,v50,z100,gancho\WObj:=Vald;
    ENDPROC
    PROC Balde_Dejar()
        MoveJ Valde_State,v600,z100,gancho\WObj:=Vald;
        MoveL Valde_1,v200,z100,gancho\WObj:=Vald;
        MoveL Valde_2,v200,z100,gancho\WObj:=Vald;
        MoveL Valde_3,v200,z100,gancho\WObj:=Vald;
        MoveJ Valde_State,v1000,z100,gancho\WObj:=Vald;
    ENDPROC
    PROC Medio_Dejar()
        MoveJ Mid_State,v100,z100,gancho\WObj:=Mid;
        MoveL Medio_1,v50,z10,gancho\WObj:=Mid;
    ENDPROC
    PROC Medio_Tomar()
        MoveJ Mid_State,v1000,z100,gancho\WObj:=Mid;
        MoveL Medio_3,v200,z100,gancho\WObj:=Mid;
        MoveL Medio_4,v200,z100,gancho\WObj:=Mid;
        MoveL Medio_1,v200,z100,gancho\WObj:=Mid;
        MoveJ Mid_State,v1000,z100,gancho\WObj:=Mid;
    ENDPROC
    PROC Soltar_Ficha()
        MoveJ Soltar_State,v400,z100,ventosa\WObj:=Mid;
        MoveL Soltar_2,v200,z100,ventosa\WObj:=Mid;
        MoveL Soltar_1,v200,z100,ventosa\WObj:=Mid;
    ENDPROC
    PROC Soltar_Volver()
        MoveL Soltar_2,v200,z100,ventosa\WObj:=Mid;
        MoveJ Soltar_State,v600,z100,ventosa\WObj:=Mid;
    ENDPROC
    PROC Medio_Dejar2()
        MoveL Medio_2,v20,z10,gancho\WObj:=Mid;
        MoveL Medio_3,v50,z100,gancho\WObj:=Mid;
        MoveJ Mid_State,v1000,z100,gancho\WObj:=Mid;
    ENDPROC
ENDMODULE