# DOOM 3: BFG Edition

<!-- ### Contents -->

### Resources
- [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Doom_3)
- [Locker Codes](https://doomwiki.org/wiki/Doom_3_locker_codes)
- [All PDAs, Locker/Codes & Video Logs](https://steamcommunity.com/sharedfiles/filedetails/?id=648937694)

### Notes
1. Copy `autoexec.cfg` to `C:\Program Files (x86)\Steam\steamapps\common\DOOM 3 BFG Edition\base`
1. Be sure to adjust `r_vidMode` to highest resolution and FPS.
1. If console is enabled, certain commands may disable achievements.

> How to adjust `r_vidMode`:
> 
> _Why?_ 
> 1. Maps directly to a single in-game setting: `Fullscreen`
> 1. Default game resolution is 720p, I'm sure you want better...
> 
> `0` yields `Disabled` for the `Fullscreen` setting. Small numbers = low resolutions, greater numbers = higher resolutions; hence, the greatest possible number is @ highest resolution and max fps.  `r_vidMode` is the count from `Disabled` to this setting. So if the mode you counted is `48` slots away, that's what you ought to set `r_vidMode` equal to!

### Parameters

| jure                  | facto                             |
| ----------------------| --------------------------------- |
| `com_allowconsole`    | developer menu                    |
| `com_skipIntroVideos` | skip intro videos                 | 
| `r_vidMode`           | monitor selection, res, and FPS   | 
| `com_engineHz`        | game FPS                          |
| `g_fov`               | multiplayer fov                   |
| `in_toggleCrouch`     | toggle crouch (hold is default)   |
| `in_toggleZoom`       | toggle ads (none is default)      |
| `_zoom`               | param to bind toggle ads to       |
| Remove Head Bobbing   |                                   |
| Video Optimizations   |                                   |