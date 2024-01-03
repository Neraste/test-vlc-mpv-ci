import python_mpv_jsonipc as mpv

player = mpv.MPV()
print(player.mpv_version)
player.terminate()
