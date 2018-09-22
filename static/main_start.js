//timelines
var basicTimeline = anime.timeline({
}
);
basicTimeline
.add({
    targets: '.title',
    easing: 'easeInOutSine',
    scale: [300, 1],
    opacity: [0,1],
    duration: 3000
  })
.add({
    targets: '.buttons',
    easing: 'easeOutExpo',
    opacity: [0,1],
    duration: 5000
})
