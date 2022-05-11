import keyboard
import pymem


dwEntityList = 0x4DD346C
dwGlowObjectManager = 0x531C078
m_iGlowIndex = 0x10488
m_iTeamNum = 0xF4


pn = "csgo.exe"


def vpe():
    pym = pymem.Pymem(pn)
    proc = pymem.process.module_from_name(pym.process_handle, "client.dll").lpBaseOfDll

    while True:

        if keyboard.is_pressed("end"):
            exit(0)
                
        glowmng = pym.read_int(proc + dwGlowObjectManager)

        for i in range(1, 32):

            player = pym.read_int(proc + dwEntityList + i * 0x10)

            if player:
                teamid = pym.read_int(player + m_iTeamNum)
                entglow = pym.read_int(player + m_iGlowIndex)

                if teamid == 2:
                    pym.write_float(glowmng + entglow * 0x38 + 0x8, float(1))
                    pym.write_float(glowmng + entglow * 0x38 + 0xC, float(1))
                    pym.write_float(glowmng + entglow * 0x38 + 0x10, float(0))
                    pym.write_float(glowmng + entglow * 0x38 + 0x14, float(1))
                    pym.write_int(glowmng + entglow * 0x38 + 0x28, 1)

                elif teamid == 3:
                    pym.write_float(glowmng + entglow * 0x38 + 0x8, float(0))
                    pym.write_float(glowmng + entglow * 0x38 + 0xC, float(1))
                    pym.write_float(glowmng + entglow * 0x38 + 0x10, float(1))
                    pym.write_float(glowmng + entglow * 0x38 + 0x14, float(1))
                    pym.write_int(glowmng + entglow * 0x38 + 0x28, 1)
    

vpe()
