import { createElement, createRef, type ComponentRef } from 'react';
import { ModularDesignVector } from '@hugocxl/vectors/react-native';
import { FastPerformanceVector } from '@hugocxl/vectors/react-native/fast-performance';
createElement(ModularDesignVector, { size: 320, ref: createRef<ComponentRef<typeof ModularDesignVector>>(), accessibilityLabel: 'Modules' });
createElement(FastPerformanceVector, { color: '#64748b', onPress: () => {} });
// @ts-expect-error DOM events are not native props
createElement(ModularDesignVector, { onClick: () => {} });
