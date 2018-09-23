//timelines
var basicTimeline = anime.timeline({
}
);
basicTimeline
.add({
    targets: '#logo',
    easing: 'easeInOutSine',
    scale: [300, 1],
    opacity: [0,1],
    duration: 2000
  })
.add({
    targets: '.buttons',
    easing: 'easeOutExpo',
    opacity: [0,1],
    duration: 4000
})
