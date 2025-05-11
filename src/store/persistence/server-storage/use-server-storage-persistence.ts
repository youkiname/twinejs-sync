import * as React from 'react';
import * as prefs from '../local-storage/prefs';
import * as stories from './stories';
import * as storyFormats from '../local-storage/story-formats';

export function useServerStoragePersistence() {
	return React.useMemo(
		() => ({
			prefs: {
				load: prefs.load,
				saveMiddleware: prefs.saveMiddleware
			},
			stories: {
				load: stories.load,
				saveMiddleware: stories.saveMiddleware
			},
			storyFormats: {
				load: storyFormats.load,
				saveMiddleware: storyFormats.saveMiddleware
			}
		}),
		[]
	);
}
