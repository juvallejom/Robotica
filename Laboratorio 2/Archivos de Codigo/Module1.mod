MODULE Module1
        CONST robtarget C_10:=[[-100,200,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_20:=[[-100,300,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_30:=[[0,300,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_40:=[[0,200,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_10:=[[-100,100,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_20:=[[-100,30,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_30:=[[-70,0,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_40:=[[-30,0,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_50:=[[0,30,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_60:=[[0,100,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_10:=[[-100,-100,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_20:=[[-100,-200,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_30:=[[-100,-150,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_40:=[[0,-150,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_50:=[[0,-100,290],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_10:=[[0,0,200],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget CambioLetra:=[[0,0,200],[1,0,0,0],[-1,1,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Home:=[[0.000354986,-0.001356089,0],[1,0,0.000000001,-0.000000001],[0,2,-3,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_10_2:=[[-100,200,290],[1,0,0,0],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_20_2:=[[-100,300,290],[1,0,0,0],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_30_2:=[[0,300,290],[1,0,0,0],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget C_40_2:=[[0,200,290],[1,0,0,0],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_10_2:=[[-100,100,290],[1,0,0,0],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_20_2:=[[-100,30,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_30_2:=[[-70,0,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_40_2:=[[-30,0,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_50_2:=[[0,30,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget D_60_2:=[[0,100,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_10_2:=[[-100,-100,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_20_2:=[[-100,-200,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_30_2:=[[-100,-150,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_40_2:=[[0,-150,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget J_50_2:=[[0,-100,290],[1,0,0,0],[0,-2,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget CambioLetra_2:=[[0,0,200],[1,0,0,0],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST jointtarget Homereal:=[[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
!***********************************************************
    !
    ! Module:  Module1
    !
    ! Description:
    !   <Insert description here>
    !
    ! Author: Usuario
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
        
        IF DI_01=1 THEN
            Homing;
            Path_Cambio;
            Path_C;
            Path_Cambio;
            Path_D;
            Path_Cambio;
            Path_J;
            Path_Cambio;
            
        ELSEIF DI_02=1 THEN
            Homingreal;
        ENDIF
        
        
        !Add your code here
    ENDPROC
    PROC Path_C()
        MoveL C_10,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL C_20,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL C_30,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL C_40,v600,z10,MarcadorA\WObj:=HomeRigth;
    ENDPROC
    PROC Path_D()
        MoveL D_10,v400,z10,MarcadorA\WObj:=HomeRigth;
        MoveL D_20,v400,z10,MarcadorA\WObj:=HomeRigth;
        MoveL D_30,v400,z10,MarcadorA\WObj:=HomeRigth;
        MoveL D_40,v400,z10,MarcadorA\WObj:=HomeRigth;
        MoveL D_50,v400,z10,MarcadorA\WObj:=HomeRigth;
        MoveL D_60,v400,z10,MarcadorA\WObj:=HomeRigth;
        MoveL D_10,v400,z10,MarcadorA\WObj:=HomeRigth;
    ENDPROC
    PROC Path_J()
        MoveL J_10,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL J_20,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL J_30,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL J_40,v600,z10,MarcadorA\WObj:=HomeRigth;
        MoveL J_50,v600,z10,MarcadorA\WObj:=HomeRigth;
    ENDPROC
    PROC Path_10()
        MoveL Target_10,v1000,z100,MarcadorA\WObj:=HomeRigth;
    ENDPROC
    PROC Path_Cambio()
        MoveL CambioLetra,v1000,z100,MarcadorA\WObj:=HomeRigth;
    ENDPROC
    PROC Homing()
        MoveJ Home,v1000,z100,MarcadorA\WObj:=HomeRigth;
    ENDPROC
    PROC Path_C2()
        MoveL C_10_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL C_20_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL C_30_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL C_40_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
    ENDPROC
    PROC Path_D2()
        MoveL D_10_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL D_20_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL D_30_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL D_40_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL D_50_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL D_60_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL D_10_2,v1000,z100,MarcadorA\WObj:=HomeRigth_2;
    ENDPROC
    PROC Path_J2()
        MoveL J_10_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL J_20_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL J_30_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL J_40_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
        MoveL J_50_2,v600,z10,MarcadorA\WObj:=HomeRigth_2;
    ENDPROC
    PROC Path_Cambio2()
        MoveL CambioLetra_2,v200,z100,MarcadorA\WObj:=HomeRigth_2;
    ENDPROC
    PROC Homingreal()
        MoveAbsJ Homereal,v1000,z100,MarcadorA\WObj:=wobj0;
    ENDPROC
ENDMODULE