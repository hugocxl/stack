import { createElement, createRef, type ComponentRef } from 'react';
import { SearchIcon as NativeSearchIcon } from '@hugocxl/icons/react-native';
import { TerminalIcon as NativeTerminalIcon } from '@hugocxl/icons/react-native/terminal';
createElement(NativeSearchIcon, { size: 24, ref: createRef<ComponentRef<typeof NativeSearchIcon>>(), accessibilityLabel: 'Search' });
createElement(NativeTerminalIcon, { color: 'red', onPress: () => {} });
// @ts-expect-error DOM events are not native props
createElement(NativeSearchIcon, { onClick: () => {} });

import { SearchIcon as SolidNativeSearchIcon } from '@hugocxl/icons/react-native/solid';
import { SearchIcon as StrokeNativeSearchIcon } from '@hugocxl/icons/react-native/stroke/search';
createElement(SolidNativeSearchIcon, { ref: createRef<ComponentRef<typeof SolidNativeSearchIcon>>(), accessibilityLabel: 'Search' });
createElement(StrokeNativeSearchIcon, { size: 16, onPress: () => {} });
// @ts-expect-error style exports retain the native prop boundary
createElement(StrokeNativeSearchIcon, { onClick: () => {} });

import { defaultColor } from '@hugocxl/icons/colors';
createElement(NativeTerminalIcon, { color: defaultColor('terminal', 'dark') });
