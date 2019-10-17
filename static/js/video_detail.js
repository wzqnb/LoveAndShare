function CourseDetail() {
}

CourseDetail.prototype.initPlayer = function () {
    var e = $("#video-info"), t = e.attr("data-video-url"), o = e.attr("data-cover-url"), a = e.attr("data-course-id"),
        i = cyberplayer("playercontainer").setup({
            width: "100%",
            height: "100%",
            file: t,
            image: o,
            autostart: !1,
            stretching: "uniform",
            repeat: !1,
            volume: 100,
            controls: !0,
            tokenEncrypt: !0,
            ak: "74cc7f67b1134030a7c37ee38a46c296"
        });
    i.on("beforePlay", function (o) {
        /m3u8/.test(o.file) && xfzajax.get({
            url: "/course/course_token/",
            data: {video: t, course_id: a},
            success: function (e) {
                if (200 === e.code) {
                    var t = e.data.token;
                    i.setToken(o.file, t)
                } else window.messageBox.showInfo(e.message), i.stop()
            },
            fail: function (e) {
                console.log(e)
            }
        })
    })
}, CourseDetail.prototype.run = function () {
    this.initPlayer()
}, $(function () {
    (new CourseDetail).run()
});
