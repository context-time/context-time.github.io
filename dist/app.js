(() => {
  const data = window.TUTORIAL;
  const chinese = document.documentElement.lang.startsWith('zh');
  const make = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  };
  for (const speaker of data.speakers) {
    const card = make('article', 'speaker-card');
    card.id = speaker.id;
    const profile = make('a', 'speaker-link');
    profile.href = speaker.profile;
    profile.target = '_blank';
    profile.rel = 'noopener noreferrer';
    const image = make('img', 'speaker-photo');
    image.src = speaker.photo;
    image.alt = '';
    image.width = 88;
    image.height = 104;
    image.loading = 'lazy';
    image.decoding = 'async';
    const name = chinese ? (speaker.chinese || speaker.name) : speaker.name;
    profile.append(image, make('h3', '', name));
    card.append(profile,
      make('p', 'speaker-role', chinese ? speaker.roleZh : speaker.role),
      make('p', 'speaker-affiliation', chinese ? speaker.affiliationZh : speaker.affiliation));
    document.querySelector('#speaker-grid').append(card);
  }
  const program = document.querySelector('#program-topics');
  data.sessions.forEach((session, index) => {
    const topic = make('li', '', chinese ? session.titleZh : session.title);
    topic.id = `session-${index + 1}`;
    program.append(topic);
  });
  document.querySelectorAll('.language-switch a').forEach(link => {
    link.addEventListener('click', () => {
      const target = new URL(link.href);
      const current = new URL(window.location.href);
      target.hash = current.hash;
      if (current.hash === '#slides' && current.searchParams.has('page')) {
        target.searchParams.set('page', current.searchParams.get('page'));
      } else {
        target.searchParams.delete('page');
      }
      link.href = target.href;
    });
  });
})();
