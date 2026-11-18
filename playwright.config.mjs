import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  use: {
    baseURL: 'http://127.0.0.1:8123',
    browserName: 'chromium',
    deviceScaleFactor: 1,
    locale: 'en-GB',
    reducedMotion: 'reduce',
    timezoneId: 'UTC',
  },
  webServer: {
    command: 'python3 -m http.server 8123 --bind 127.0.0.1',
    url: 'http://127.0.0.1:8123/',
  },
});
