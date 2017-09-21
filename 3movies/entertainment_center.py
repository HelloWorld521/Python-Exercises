# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

overwatch = media.Movie("Overwatch","守望者们回归",
	"https://overwatch.nos.netease.com/2/media/Wallpapers/Genji_wallpaper/2048x2048.jpg",
	"https://flv.bn.netease.com/videolib3/1506/26/cJtFW2189/HD/cJtFW2189-mobile.mp4")

school_of_rock = media.Movie("School of Rock"," Using rock music to learn",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74")

spider_gay = media.Movie("美队3 内战","搞笑蜘蛛侠",
	"https://p1.ifengimg.com/a/2016_19/ea0b92b08ab62d2_size47_w550_h275.jpg",
	"https://www.youtube.com/watch?time_continue=16&v=Wa5yWjsjGoI")

overwatch2 = media.Movie("双龙","双龙",
	"https://overwatch.nos.netease.com/2/media/videos/dragons-animated-short.jpg",
	"https://flv.bn.netease.com/videolib3/1605/16/nTaMi2329/HD/nTaMi2329-mobile.mp4")

overwatch3 = media.Movie("虚幻争霸","虚幻争霸试玩",
	"https://i.ytimg.com/vi/l-TAaE5raeU/hqdefault.jpg",
	"https://www.youtube.com/watch?v=l-TAaE5raeU")

overwatch4 = media.Movie("LOL","盘点lol最强操作",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLfycX_SZr4pT-UVddhr0FdcN67cX1rwFM21PPH3glYPETzGtT",
	"https://r.plures.net/plu/tplayer/video-iath80mu.swf?vid=w0162pdtuoi&auto=1")

movies = [overwatch, school_of_rock, spider_gay, overwatch2, overwatch3, overwatch4]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
#print(media.Movie.__doc__)