function CourseDetail() {
}


CourseDetail.prototype.initPlayer = function () {
    var e = $("#video-info");
    var videourl = e.attr("data-video-url");
    var cover = e.attr("data-cover-url");
    var id = e.attr("data-course-id");


    var player = cyberplayer("playercontainer").setup({
        width: 640,
        height: 480,
        file: videourl,
        image: cover,
        title: "LoveAndShare",
        autostart: !1,
        stretching: "uniform",
        repeat: !1,
        volume: 100,
        controls: true,
        tokenEncrypt: !0,
        ak: "74cc7f67b1134030a7c37ee38a46c296"
    });
    player.on("beforePlay", function (e) {

        if (!/m3u8/.test(e.file)) {
            return;
        }
        $ajax.get({
            url: "/course/course_token/",
            data: {video: videourl, course_id: id},
            success: function (result) {
                if (result['code'] === 200) {
                    var token = result['data']['token'];
                    player.setToken(e.file, token);
                } else {
                    alert('token错误！');
                }
            },
            fail: function (error) {
                console.log(error)
            }
        })
    })
}, CourseDetail.prototype.run = function () {
    this.initPlayer()
}, $(function () {
    (new CourseDetail).run()
});
