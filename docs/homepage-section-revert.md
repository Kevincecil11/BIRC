# Desktop homepage section rollback

The two redesigns are isolated and can be reverted independently. Both loaders live at the bottom of `assets/voices-grid.js` inside clearly labelled comments.

## Revert Knowledge Sessions only

Remove or comment out:

```js
loadHomeFeature('home-knowledge-living-columns','20260820a');
```

The original `#knowledge-sessions` markup in `desktop.html` remains untouched and will render again. The related `home-knowledge-living-columns.css` and `.js` files may remain unused or be deleted.

## Revert Experience Zones only

Remove or comment out:

```js
loadHomeFeature('home-experience-stage-rail','20260820a');
```

The original `#zones` atlas markup in `desktop.html` remains untouched and will render again. The related `home-experience-stage-rail.css` and `.js` files may remain unused or be deleted.

## Revert both

Remove both loader calls. Touch `publish-refresh.html` in the same commit so GitHub Pages republishes the JS-only rollback.
