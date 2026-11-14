(() => {
  const total = 104;
  const isChinese = document.documentElement.lang === 'zh-CN';
  const copy = isChinese ? {
    total: '共 104 页',
    page: (n) => `第 ${n} 页，共 ${total} 页`,
    loading: '正在加载课件…',
    error: '课件加载失败，请重试。',
    retry: '重试',
    zoomIn: '放大',
    zoomOut: '适应宽度',
  } : {
    total: `of ${total}`,
    page: (n) => `Slide ${n} of ${total}`,
    loading: 'Loading slide…',
    error: 'This slide could not be loaded.',
    retry: 'Retry',
    zoomIn: 'Zoom in',
    zoomOut: 'Fit to width',
  };

  const controls = document.querySelector('#reader-controls');
  const viewport = document.querySelector('#reader-viewport');
  const canvas = document.querySelector('#reader-slide');
  const context = canvas.getContext('2d');
  const input = document.querySelector('#reader-page');
  const status = document.querySelector('#reader-status');
  const previous = document.querySelector('#reader-prev');
  const next = document.querySelector('#reader-next');
  const zoom = document.querySelector('#reader-zoom');
  const language = document.querySelector('#reader-language');
  let current = 1;
  let request = 0;

  function show(page) {
    current = Number.isInteger(page) ? Math.min(total, Math.max(1, page)) : 1;
    const id = ++request;
    const url = new URL(window.location.href);
    url.searchParams.set('page', current);
    history.replaceState(null, '', url);
    language.search = url.search;
    input.value = current;
    previous.disabled = current === 1;
    next.disabled = current === total;
    viewport.scrollTo(0, 0);
    viewport.setAttribute('aria-busy', 'true');
    status.textContent = copy.loading;
    canvas.setAttribute('aria-label', copy.loading);
    context.clearRect(0, 0, canvas.width, canvas.height);

    const picture = new Image();
    picture.onload = () => {
      if (id !== request) return;
      canvas.width = picture.naturalWidth;
      canvas.height = picture.naturalHeight;
      context.drawImage(picture, 0, 0);
      canvas.setAttribute('aria-label', copy.page(current));
      viewport.setAttribute('aria-busy', 'false');
      status.textContent = copy.page(current);
    };
    picture.onerror = () => {
      if (id !== request) return;
      viewport.setAttribute('aria-busy', 'false');
      canvas.setAttribute('aria-label', copy.error);
      status.textContent = copy.error + ' ';
      const retry = document.createElement('button');
      retry.type = 'button';
      retry.textContent = copy.retry;
      retry.addEventListener('click', () => show(current));
      status.append(retry);
    };
    picture.src = `assets/slides/2026-11-14/${String(current).padStart(3, '0')}.webp`;
  }

  if (!context) {
    status.textContent = copy.error;
    return;
  }
  controls.hidden = false;
  input.max = total;
  document.querySelector('#reader-total').textContent = copy.total;
  previous.addEventListener('click', () => show(current - 1));
  next.addEventListener('click', () => show(current + 1));
  controls.addEventListener('submit', (event) => {
    event.preventDefault();
    show(input.valueAsNumber);
  });
  zoom.addEventListener('click', () => {
    const active = viewport.classList.toggle('is-zoomed');
    zoom.setAttribute('aria-pressed', String(active));
    zoom.textContent = active ? copy.zoomOut : copy.zoomIn;
    if (!active) viewport.scrollTo(0, 0);
  });
  canvas.addEventListener('contextmenu', (event) => event.preventDefault());
  viewport.addEventListener('keydown', (event) => {
    if (viewport.classList.contains('is-zoomed')) return;
    const pages = {ArrowLeft: current - 1, ArrowRight: current + 1, Home: 1, End: total};
    if (!Object.hasOwn(pages, event.key)) return;
    event.preventDefault();
    show(pages[event.key]);
  });

  show(Number(new URLSearchParams(location.search).get('page')));
})();
