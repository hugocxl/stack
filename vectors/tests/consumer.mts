import { createElement, createRef } from 'react';
import { ModularDesignVector } from '@hugocxl/vectors/react';
import { FastPerformanceVector } from '@hugocxl/vectors/react/fast-performance';

createElement(ModularDesignVector, { size: 320, ref: createRef<SVGSVGElement>(), 'aria-label': 'Modular design' });
createElement(FastPerformanceVector, { color: 'red', className: 'hero', onClick: event => event.currentTarget.focus() });
// @ts-expect-error size must be numeric
createElement(ModularDesignVector, { size: 'large' });

import { ModularDesignVector as modularSvg } from '@hugocxl/vectors/js';
import { ModularDesignVector as rootSvg } from '@hugocxl/vectors';
import { ModularDesignVector as singleSvg } from '@hugocxl/vectors/js/modular-design';
const svg: string = modularSvg;
const same: string = rootSvg;
const single: string = singleSvg;
// @ts-expect-error unknown vectors are not exported
import { NotAVector } from '@hugocxl/vectors/react';
