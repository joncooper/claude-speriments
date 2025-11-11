# ICEBOX - Future Enhancements

Ideas and features to explore in future iterations of Sideshow.

## Core Features

### Highlight Improvements
- [ ] **Multiple highlight colors** - Let users choose from color palette
- [ ] **Nested highlights** - Support overlapping highlights
- [ ] **Highlight threads** - Multiple annotations per highlight
- [ ] **@mentions** - Tag people in annotations (requires user system)
- [ ] **Emoji reactions** - Quick reactions to highlights

### Editing & Persistence
- [ ] **Auto-save** - Save drafts automatically every N seconds
- [ ] **Version history** - Track changes over time
- [ ] **Conflict resolution** - Handle concurrent edits gracefully
- [ ] **Undo/redo** - Command history for edits
- [ ] **Smart highlight preservation** - Maintain highlights when markdown edited

### Content Types
- [ ] **Code syntax highlighting** - Detect and highlight code blocks
- [ ] **Multiple files** - Support multi-file gists like GitHub
- [ ] **Rich text editor** - WYSIWYG option alongside markdown
- [ ] **Image uploads** - Embed images directly
- [ ] **PDF export** - Download as PDF with annotations

### Sharing & Collaboration
- [ ] **Custom short URLs** - Let users pick their own slug
- [ ] **QR codes** - Generate QR code for easy mobile sharing
- [ ] **Embed widget** - iframe embed for other sites
- [ ] **Social preview** - OpenGraph tags for nice link previews
- [ ] **View analytics** - Track views (privacy-conscious)
- [ ] **Expiring links** - Links that expire after N days
- [ ] **Password protection** - Optional password for sensitive gists

### Search & Organization
- [ ] **Gist library** - List/search user's own gists
- [ ] **Tags** - Organize gists with tags
- [ ] **Folders** - Group related gists
- [ ] **Search annotations** - Full-text search across all annotations
- [ ] **Favorites** - Star/favorite gists

### UI/UX Enhancements
- [ ] **Dark mode** - Dark theme option
- [ ] **Customizable layout** - Adjust sidebar width, position
- [ ] **Keyboard shortcuts** - Power user shortcuts
- [ ] **Mobile app** - Native iOS/Android app
- [ ] **Responsive design** - Better mobile experience
- [ ] **Accessibility** - ARIA labels, screen reader support
- [ ] **Print stylesheet** - Clean print layout

### Performance
- [ ] **Lazy loading** - Load annotations on demand
- [ ] **Virtual scrolling** - For documents with many highlights
- [ ] **Service worker** - Offline support with PWA
- [ ] **CDN hosting** - Serve static assets from CDN

## Technical Improvements

### Testing
- [ ] **Unit tests** - Test core logic with Vitest
- [ ] **Integration tests** - Test Firebase interactions with emulator
- [ ] **E2E tests** - Browser tests with Playwright
- [ ] **Visual regression** - Screenshot comparison tests

### Developer Experience
- [ ] **ESLint** - Linting rules for code quality
- [ ] **Prettier** - Code formatting
- [ ] **Husky** - Pre-commit hooks
- [ ] **CI/CD** - Automated testing and deployment
- [ ] **Component library** - Reusable UI components

### Security
- [ ] **Rate limiting** - Prevent abuse (via Firebase extensions)
- [ ] **Content moderation** - Flag inappropriate content
- [ ] **Report abuse** - Let users report violations
- [ ] **CAPTCHA** - Prevent automated abuse

### Data & Analytics
- [ ] **Usage analytics** - Privacy-conscious analytics (Plausible, etc.)
- [ ] **Error tracking** - Sentry or similar for error monitoring
- [ ] **Performance monitoring** - Track Core Web Vitals
- [ ] **A/B testing** - Test feature variations

### Integrations
- [ ] **GitHub import** - Import gists from GitHub
- [ ] **Obsidian plugin** - Sync with Obsidian notes
- [ ] **Browser extension** - Clip web pages as annotated gists
- [ ] **API** - Public API for programmatic access
- [ ] **Webhooks** - Notify on gist updates

## Advanced Features

### AI-Powered
- [ ] **AI summaries** - Generate TL;DR of document
- [ ] **AI-suggested annotations** - Claude suggests relevant notes
- [ ] **Smart highlighting** - AI suggests important sections
- [ ] **Translation** - Translate annotations to other languages

### Collaborative
- [ ] **Multiplayer mode** - Real-time collaborative editing
- [ ] **Comments** - Discussion threads on highlights
- [ ] **Suggested edits** - Propose changes (like Google Docs)
- [ ] **Peer review** - Structured review workflow

### Academic
- [ ] **Citations** - Proper citation formatting
- [ ] **Bibliography** - Auto-generate bibliography
- [ ] **Reference linking** - Link between related gists
- [ ] **Export to LaTeX** - For academic papers

### Enterprise
- [ ] **Team workspaces** - Shared team libraries
- [ ] **SSO** - Single sign-on for organizations
- [ ] **Admin controls** - Manage users and permissions
- [ ] **Audit logs** - Track all actions
- [ ] **Custom branding** - White-label option

## Infrastructure

### Scaling
- [ ] **Database optimization** - Index tuning, query optimization
- [ ] **Caching layer** - Redis for frequently accessed gists
- [ ] **CDN for assets** - Faster global delivery
- [ ] **Multi-region** - Deploy to multiple Firebase regions

### Monitoring
- [ ] **Uptime monitoring** - Alert on downtime
- [ ] **Cost tracking** - Monitor Firebase usage and costs
- [ ] **Performance budgets** - Set and enforce perf budgets

### Backup & Recovery
- [ ] **Automated backups** - Regular Firestore exports
- [ ] **Data export** - Let users export all their data
- [ ] **Import/restore** - Restore from backups

## Research & Experiments

### Novel Interactions
- [ ] **Voice annotations** - Record audio annotations
- [ ] **Video annotations** - Annotate video transcripts
- [ ] **3D highlighting** - Novel visualization techniques
- [ ] **Spatial annotations** - AR/VR annotations

### Alternative Architectures
- [ ] **Local-first** - CRDT-based local-first architecture
- [ ] **P2P sharing** - WebRTC for direct sharing
- [ ] **Blockchain** - Decentralized storage (probably overkill)

### Accessibility Research
- [ ] **Voice control** - Voice commands for highlighting
- [ ] **Screen reader optimization** - Advanced a11y features
- [ ] **Dyslexia-friendly** - Font and spacing options

## Community

### Open Source
- [ ] **Public roadmap** - Let community vote on features
- [ ] **Plugin system** - Let developers extend Sideshow
- [ ] **Themes** - Community-created themes
- [ ] **Templates** - Starter templates for common use cases

## Priority Matrix

### High Value, Low Effort (Do Soon)
- Dark mode
- Multiple highlight colors
- Auto-save
- Keyboard shortcuts
- Gist library/list view

### High Value, High Effort (Plan Carefully)
- Smart highlight preservation
- Code syntax highlighting
- Mobile app
- Collaborative editing
- Search annotations

### Low Value, Low Effort (Nice to Have)
- Custom short URLs
- QR codes
- Social preview tags
- Print stylesheet

### Low Value, High Effort (Probably Not)
- Blockchain storage
- AR/VR annotations
- Video annotations

## Notes

- **Start simple**: Focus on core use case first
- **User feedback**: Build what users actually want
- **Performance**: Don't sacrifice speed for features
- **Privacy**: Always respect user privacy
- **Cost**: Stay within Firebase free tier for now

---

**Last updated:** November 2025
