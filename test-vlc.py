import vlc

instance = vlc.Instance()
player = instance.media_player_new()
print(vlc.libvlc_get_version().decode())
