// Single source of truth for site content.
// Sourced from the existing rockypointclub.com (crawled May 2026).
// Members can edit this file to update copy without touching components.

export const club = {
  name: "Rocky Point Club",
  tagline: "A family club on Long Island Sound since 1927",
  established: 1927,
  address: {
    line1: "60 Rocky Point Road",
    line2: "Old Greenwich, CT 06870",
  },
  coords: { lat: 41.017263, lng: -73.55868699999996, label: '41°1’1" N, 73°33’30" W' },
  phones: [
    { label: "Gatehouse", value: "203-637-2397" },
    { label: "Manager / Grounds", value: "203-637-3620" },
  ],
  email: "info@rockypointclub.com",
  emails: {
    general: "info@rockypointclub.com",
    juniorSailing: "jrsailing@rockypointclub.com",
    adultSailing: "sailing@rockypointclub.com",
  },
  staff: [
    { name: "Jimmy Ramaley", role: "Manager" },
    { name: "Pete Cantazaro", role: "Grounds Manager" },
  ],
  facebook: "https://www.facebook.com/groups/rockypointclub",
};

export const heroQuote = {
  text:
    "A marine view as picturesque as any that can be found in the world — a little beach of solid stone, a little bay, a slender rocky peninsula, and a lighthouse in the distance, all properly combined with passing boats to suggest the charm of the great ocean.",
  attribution: "Edward Bigelow, 1927",
};

export const welcome = {
  heading: "Welcome to Rocky",
  body:
    "Tucked onto a rocky peninsula reaching into Long Island Sound, Rocky Point Club has been a summer home for Old Greenwich families since 1927. Sailing, swimming, and good company — by the water, the way it has always been.",
  cta: { label: "Explore membership", href: "/membership" },
};

export const nav = [
  { label: "About", href: "/about" },
  { label: "Membership", href: "/membership" },
  { label: "Aquatics", href: "/aquatics" },
  { label: "Sailing", href: "/sailing" },
  { label: "Events", href: "/events" },
  { label: "Contact", href: "/contact" },
];

export const highlights = [
  {
    title: "Junior Sailing",
    blurb:
      "A six-week program for ages 6–17, from first time in an Opti to the racing team — taught the way Rocky has always taught it.",
    href: "/sailing",
  },
  {
    title: "Aquatics",
    blurb:
      "Swim team, dive team, lessons, and water polo on the Sound. Competitive when it counts, joyful all summer.",
    href: "/aquatics",
  },
  {
    title: "Summer at the Point",
    blurb:
      "Cocktail evenings, the Fourth of July fireworks, BYO nights, and the regatta — the social calendar that holds the season together.",
    href: "/events",
  },
];

export const history = {
  title: "History",
  intro:
    "Rocky Point Club has been part of Old Greenwich life for nearly a century — through hurricanes, the Depression, and the steady hands of members who rebuilt it more than once.",
  timeline: [
    {
      year: "1927",
      title: "The Rocky Point Bathes open",
      body:
        "William W. Schofield opens the Rocky Point Bathes on June 1, 1927, on a peninsula long admired for its view of Long Island Sound.",
    },
    {
      year: "1938–1941",
      title: "Depression and storm",
      body:
        "Schofield weathers the Great Depression and the 1938 hurricane. An offer to sell to the Town of Greenwich for $100,000 in 1940 is rejected in favor of Tod's Point. The property goes into foreclosure on December 15, 1941.",
    },
    {
      year: "1943",
      title: "The White family arrives",
      body:
        "On April 23, 1943, John Hazen White purchases Rocky Point Club for $35,000.",
    },
    {
      year: "1950",
      title: "Rebuilt by its members",
      body:
        "A devastating hurricane destroys the club. Members rebuild it themselves through coordinated weekend work shifts — the first of several times Rocky is saved by the people who use it.",
    },
    {
      year: "1953–1954",
      title: "The members buy Rocky",
      body:
        "The club is incorporated in 1953. In 1954 the White family sells Rocky to its members for $79,088.00.",
    },
  ],
  philosophy:
    'Under the Whites, Rocky was deliberately kept a family club centered on children learning to sail. They refused to add a dining room or a bar, insisting Rocky would never become "just a parking place for kids." Members have guarded that character ever since.',
};

export const board = {
  title: "Board of Governors",
  year: 2026,
  officers: [
    { role: "President", name: "Brian Amen" },
    { role: "Vice-President", name: "John Palmer" },
    { role: "Secretary", name: "Heather DeVries" },
    { role: "Treasurer", name: "Doug Fenton" },
    { role: "Assistant Treasurer", name: "Chiara Carter" },
  ],
  chairs: [
    { role: "Aquatics", name: "Kara Mendelsohn" },
    { role: "Buildings & Grounds", name: "Adrien Campbell" },
    { role: "Commodore / Adult Sailing", name: "Catherine Keenan" },
    { role: "Communications", name: "Courtney Murphy" },
    { role: "Entertainment", name: "Paula Brandes" },
    { role: "House", name: "Jane Anderson" },
    { role: "Junior Sailing", name: "Edward Carroll, Jr." },
    { role: "Waterfront", name: "Carl Wunderlich" },
  ],
};

export const membership = {
  title: "Membership",
  intro:
    "Rocky has always kept its membership small and family-oriented. Prospective members are introduced through a sponsor and seconder; the categories below cover the stages of a Rocky membership over a lifetime.",
  applyNote:
    "New member inquiries begin with a sponsor and a seconder from the current membership. Reach out to the Membership Committee through the club office to start a conversation.",
  categories: [
    {
      name: "Active Membership",
      summary:
        "The standard family membership — full access to sailing, aquatics, the waterfront, and the social calendar for the household.",
    },
    {
      name: "Senior Membership",
      summary:
        "For members who are 65 years of age and have been members for 20 years, recognizing a lifetime at Rocky with adjusted dues.",
    },
    {
      name: "Non-Resident Membership",
      summary:
        "For Active, Senior, or Inactive members who move their primary residence 50 or more miles from Greenwich.",
    },
    {
      name: "Inactive Membership",
      summary:
        "Hold your place in the club through a season away, with the right to return to active status.",
    },
    {
      name: "Return to Active",
      summary:
        "The path back from Inactive or Non-Resident status to a full Active membership.",
    },
    {
      name: "Senior Waiting List",
      summary:
        "Members approaching Senior eligibility can join the waiting list as places become available.",
    },
  ],
};

export const aquatics = {
  title: "Aquatics",
  intro:
    "Swimming at Rocky runs all summer — from first lessons off the dock to championship dual meets against the strongest clubs in the division.",
  registrationNote: "Aquatics registration opens April 12th.",
  programs: [
    {
      name: "Swim Team",
      ages: "School-age and up",
      schedule: "Monday–Saturday",
      body:
        'Practices start after school in early June and move to mornings for the summer; sessions run 60–90 minutes with twice-weekly "Starts & Turns" clinics. Five dual meets against Division 1 clubs lead into the Divisional and County Championships for qualified swimmers.',
    },
    {
      name: "Swim Lessons",
      ages: "Ages 4–14 (as of June 15)",
      schedule: "Tuesday–Friday",
      body:
        'Lessons meet Tuesday–Friday as scheduled. All swim team members aged 14 and under participate. The season ends with a "Lesson Meet" where swimmers show their progress.',
    },
    {
      name: "Pre-Team",
      ages: "Age 5+",
      schedule: "Tuesday–Friday",
      body:
        "The bridge between lessons and the swim team — building endurance, strokes, and confidence for first-time competitors.",
    },
    {
      name: "Dive Team & Diving Lessons",
      ages: "School-age and up",
      schedule: "Mon–Sat (team) · Tue–Fri (lessons)",
      body:
        "Springboard diving instruction and a competitive dive team that travels to meets alongside the swim team.",
    },
    {
      name: "Water Polo",
      ages: "Mini: 10 & under · Juniors: 11–13 · Seniors: 14–17",
      schedule: "Monday–Friday",
      body:
        'Age-grouped water polo with safety first — coaches evaluate readiness so, in the program’s words, "we want to make sure everyone is safe."',
    },
  ],
};

export const sailing = {
  title: "Sailing",
  intro:
    'Sailing is the heart of Rocky. "The goal of our program is to teach sailing in a safe and fun environment while following US Sailing guidelines."',
  junior: {
    title: "Junior Sailing",
    body:
      "An active program for roughly 40–50 children ages 6–16, sailing Optis, Fevas, and Ideal 18s. Summer 2026 offers a six-week program running June 23rd through July 31st; members register by May 15th.",
    levels: [
      {
        name: "Little Puffs",
        ages: "6–8",
        detail:
          "Introduction to sailing aboard Ideal 18s with an instructor onboard. Tuesdays–Fridays, 10:30 am–12:30 pm.",
      },
      {
        name: "Opti 1",
        ages: "8–11",
        detail:
          "Independent boat handling. Mondays 9:25 am–12:10 pm; Tuesdays–Fridays 1:00–4:00 pm.",
      },
      {
        name: "Opti 2 Racing Team",
        ages: "10–15",
        detail:
          "Racing rules and strategy; requires mastering Opti 1 skills. Mondays 9:05–11:50 am; Tuesdays–Fridays 1:45–4:45 pm.",
      },
      {
        name: "Feva & Laser 4.7 / Radial",
        ages: "12–17",
        detail:
          "Fast double- and single-handed boats with a focus on technique; requires Opti 2 mastery and minimum weight guidance. Mondays 9:05–11:50 am; Tuesdays–Fridays 1:30–4:30 pm.",
      },
    ],
    requirements: [
      "Pass the mandatory swim test",
      "USCG-approved life vest with attached whistle",
      "Signed Rocky Liability and Medical Release form",
      "JSALIS membership ($75 first child, $100 for two, $125 for three or more)",
    ],
    costNote:
      "Member fees are billed directly to your account. Private lessons are $80/hour. Non-members pay by check.",
    contact: "jrsailing@rockypointclub.com",
  },
  adult: {
    title: "Adult Sailing",
    body:
      "Sailing courses and fleet usage for adult members. Members who wish to skipper the club's Ideal 18s independently earn certified skipper status and complete the Fleet Usage Agreement Certification annually. The program includes organized regattas and recreational sailing.",
    requirements: [
      "Properly fitted life jacket and appropriate footwear",
      "Signed Fleet Usage Agreement for class participation",
      "Certified skipper status for independent Ideal 18 use (renewed annually)",
    ],
    contact: "sailing@rockypointclub.com",
  },
};

export const events = {
  title: "Events",
  intro:
    "The social season at Rocky is woven through the summer — read the Rocky Pointer bulletin for the full, up-to-date calendar.",
  recurring: [
    { name: "Spring Social", when: "Spring", body: "The season opener as the club comes back to life for the year." },
    { name: "June Cocktails", when: "June", body: "An evening on the lawn as summer gets underway." },
    { name: "Father's Day Breakfast", when: "June", body: "A morning tradition by the water." },
    { name: "Fourth of July Fireworks", when: "July 4", body: "The signature night of the Rocky calendar, with guest registration for the evening." },
    { name: "BYO Nights", when: "July–August", body: "Bring-your-own evenings throughout the high summer." },
    { name: "Regatta", when: "Summer", body: "The club regatta — racing and shoreside celebration." },
    { name: "Jaws Dinner", when: "Summer", body: "A beloved themed club dinner." },
    { name: "Members' Night", when: "Summer", body: "An evening for the membership to gather." },
    { name: "Point-to-Point Swim", when: "Summer", body: "The open-water swim across the bay." },
    { name: "Mah Jongg", when: "Ongoing", body: "Regular gatherings through the season." },
  ],
};

export const members = {
  title: "Members",
  intro:
    "The members-only area — photo directory, dues & fees, forms, the Rocky Pointer bulletin archive, tennis, and club video — is moving to a secure member login.",
  stageTwoNote:
    "This portal is coming in stage two. For now, members continue to use the existing site for directory and forms. If you need a form or document in the meantime, contact the club office.",
  plannedSections: [
    "Photo Directory",
    "Dues & Fees",
    "Member Forms",
    "Rocky Pointer Bulletin Archive",
    "Tennis",
    "Club Video & Photo Album",
    "Contact Info",
  ],
};
