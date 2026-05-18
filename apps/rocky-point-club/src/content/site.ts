// VERBATIM content from rockypointclub.com (crawled May 2026).
//
// PRINCIPLE: This rebuild modernizes the *look, structure, and
// maintainability* of the site only. The words are the club's own and must
// not be paraphrased or rewritten. When the live site's copy changes, edit
// the strings here to match — do not "improve" the wording. Any rewriting of
// copy is a decision for club members, not this codebase.
//
// Punctuation, spelling, and capitalization are reproduced as they appear on
// the live site (including the club's own quotes and quirks).

export const club = {
  name: "Rocky Point Club",
  legalName: "The Rocky Point Club, Inc.",
  address: {
    line1: "60 Rocky Point Road",
    line2: "Old Greenwich, CT 06870",
  },
  coordsLine: `Lat 41º1'1" N   Long 73º33'30"W`,
  email: "info@rockypointclub.com",
  phones: {
    gatehouse: "203-637-2397",
    managerGrounds: "203-637-3620",
  },
  staff: ["Jimmy Ramaley, Manager", "Pete Cantazaro, Grounds Manager"],
  emails: {
    general: "info@rockypointclub.com",
    juniorSailing: "jrsailing@rockypointclub.com",
    sailing: "sailing@rockypointclub.com",
    secretary: "secretary@rockypointclub.com",
  },
};

// Top-level navigation mirrors the live site's own section names.
export const nav = [
  { label: "About", href: "/about" },
  { label: "Aquatics", href: "/aquatics" },
  { label: "Entertainment", href: "/entertainment" },
  { label: "Sailing", href: "/sailing" },
  { label: "Contact", href: "/contact" },
];

export const bigelowQuote = {
  text:
    "A marine view as picturesque as any that can be found in the world - a little beach of solid stone, a little bay, a slender rocky peninsula, and a lighthouse in the distance, all properly combined with passing boats to suggest the charm of the great ocean.",
  attribution:
    "Written by Edward Bigelow, publisher of The Guide to Nature, as he looked out over the waters of Long Island Sound from Rocky Point in 1927.",
};

export const home = {
  heading: "Welcome",
  bulletinLine:
    "Read our bulletin for Rocky updates, activities, events and more!",
  admissionsCta:
    "Interested in joining Rocky Point Club? Learn more about the admissions process here.",
};

// Section cards on the home page use only the club's own section names —
// no marketing copy is invented.
export const homeSections = [
  { label: "About", href: "/about" },
  { label: "Aquatics", href: "/aquatics" },
  { label: "Sailing", href: "/sailing" },
  { label: "Entertainment", href: "/entertainment" },
];

export const history = {
  heading: "About Rocky Point",
  attribution: bigelowQuote.attribution,
  beachQuote:
    "“The beach development is, as claimed by local real estate agents, the best in the world.’ Skilled engineering and enormous expenditures for several years have brought it to marvelous perfection in beauty, comfort, and convenience”. E.F. Bigelow",
  briefHistoryLabel: "A brief history...",
  paragraphs: [
    "William W. Schofield, with grand plans for the whole Rocky Point – Meadowbank area, was the founder. The Rocky Point Bathes opened June 1st 1927.",
    "Scholfield weathered the Great Depression of the 30’s and the Great Hurricane of 1938, but by 1940, with the threat of war looming, he offered to sell Rocky to the Town of Greenwich for $100,000. His offer was rejected in favor of the 147 acre Tod’s Point property. Foreclosure procedures were completed on December 15, 1941. Mortgage holders kept Rocky open the next summer and tried to promote the use of the club.",
    "On April 23, 1943, John Hazen White bought Rocky Point Club for $35,000.",
    "Happy and John White owned the club until 1953. They felt strongly that it should be a family – oriented club with no dining room or bar. They wanted most of the activities planned for children who wanted to learn to sail. They were adamant that they would never let Rocky become “ Just a parking place for kids.”",
    "On November 24, 1950, a hurricane flattened Rocky, the club virtually disappeared. The first reaction was shock; the second was to “go get the wood.” The members rebuilt the club. A rigorous schedule was set up for the four shifts each weekend from early December until opening day.",
    "In 1953 Rocky was incorporated and in 1954 the White family sold Rocky to the members. The purchase price was $79,088.00. The property at the end of Meadowbank was offered for $15,000 but after considerable deliberation and controversy, the offer was turned down. There were members who feared Rocky might get “grand ideas.” The number of memberships at the Rocky Point Club has been restricted through the years.",
  ],
};

export const board = {
  heading: "2026 Board of Governors",
  officers: [
    { role: "President", name: "Brian Amen" },
    { role: "Vice-President", name: "John Palmer" },
    { role: "Secretary", name: "Heather DeVries" },
    { role: "Treasurer", name: "Doug Fenton" },
    { role: "Assist. Treasurer", name: "Chiara Carter" },
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

export const aquatics = {
  heading: "Aquatics Programs Overview",
  registrationLine: "Registration for aquatics programs will open on April 12th.",
  programs: [
    {
      name: "Swim Team",
      paragraphs: [
        "The Swim Team meets Monday through Saturday, beginning after school toward the beginning of June, and transitioning to morning practices. Practices are 60-90 minutes in length. “Starts & Turns” sessions are offered 2x per week to help swimmers work on these critical skills - block starts and flip turns. There are 5 “Dual Meets” with other Division 1 clubs, followed by Divisional Championships and County Championships at the end of the season (must qualify).",
      ],
    },
    {
      name: "Pre-Team",
      paragraphs: [
        "Pre-team meets daily Tuesday - Friday, typically in the afternoon. It is geared toward children age 5 years old by June 15 (and older) who can swim at least 1 length of the big pool WITHOUT assistance, but are not yet ready for the swim team. Pre-team culminates in a 1-2 Pre-team Meets with another club toward the end of the season. Evaluations will be held in early June to determine if children are ready for the Pre-team. There is no pre-team on days when the Swim Team has a meet.",
      ],
    },
    {
      name: "Swim Lessons",
      paragraphs: [
        "Swim lessons meet daily Tuesday - Friday, as scheduled. Swim lessons are available to all swimmers between the ages of 4-14 years (as of June 15). Children do NOT need to be on swim team, however all swim team members 14&U are expected to take a swim lesson as well. Swim lessons culminate in the “Lesson Meet” at the end of the season for all swimmers to show their progress! There are no swim lessons on days when the Swim Team has a meet.",
      ],
    },
    {
      name: "Diving Team",
      paragraphs: [
        "The Dive Team meets Monday through Saturday, beginning after school toward the beginning of June, and transitioning to morning practices. Practices are 60 minutes in length. There are 5 “Dual Meets” and County Championships at the end of the season (must qualify).",
      ],
    },
    {
      name: "Diving Lessons",
      paragraphs: [
        "Dive lessons meet daily Tuesday - Friday, as scheduled. Dive lessons are available to all swimmers between the ages of 4-14 years (as of June 15). Children do NOT need to be on dive team, however all dive team members 14&U are expected to take a dive lesson as well. Dive lessons culminate in the “Lesson Meet” at the end of the season for all divers to show their progress! There are no dive lessons on days when the Swim Team has a meet.",
      ],
    },
    {
      name: "Synchronized Swimming",
      paragraphs: [
        "“Synchro” is open to both boys and girls. Swimmers will be grouped together with other swimmers of their age &/or ability. These groupings are generally done by age and are at the discretion of the Synchro Chair(s) and the Synchro Coach. Synchro groups meet 2x per week, culminating in the spectacular Synchro Show at the end of the season.",
      ],
    },
    {
      name: "Water Polo",
      paragraphs: [
        "Water Polo Teams practice daily Monday - Friday. For anyone new to the RPC water polo program and considering participation in water polo only, there will be a swim evaluation and coaches will evaluate whether your child is sufficiently water safe to participate in the water polo team.",
        "As it relates to participation in the water polo teams, please make sure that your player is a strong enough and confident enough swimmer for the practices and games. We want to make sure everyone is safe. Even after the evaluation, if the water polo coaches notice that your player is not strong enough, they will let you know and may suggest he/she attend some swim practices to strengthen that ability.",
        "While we recognize that many players have commitments to outside teams, we encourage players to attend practice whenever possible for the purpose of team building and for coaches to get to know players. Every effort will be made to give players playing time during games, with the understanding that this is a competitive league and our goal is to win, particularly in the championship games.",
        "Rocky typically fields Junior A & B teams, as well as Mini A & B teams. Evaluations and rostering will be done during the first week of practice by the Head Water Polo Coach in conjunction with Coach Lowe. Once the rosters are submitted to FCSL, they are set for the season. The B teams will be competing in Division 3.",
      ],
      ages: [
        "Mini : 10 & Under",
        "Juniors : 11-13",
        "Seniors : 14-17",
        "A players age is determined on June 15th each year under FCSL Rules.",
      ],
    },
  ],
};

export const sailing = {
  heading: "Sailing Information",
  welcome: "Welcome to Rocky’s Sailing Program!",
  junior: {
    heading: "Junior Sailing Program & Mandatory Forms",
    intro:
      "Rocky Point Club has a long history of enthusiastic amateur sailing. We have a very active Opti, Feva and Ideal 18 sailing program for 40-50 children ranging in age from 6-16 years. The goal of our program is to teach sailing in a safe and fun environment while following US Sailing guidelines. The program generally runs for 6 weeks from the last week in June through the first week in August.",
    requirements: [
      "All sailing courses require the participant to have his /her own boat or rent one",
      "All sailors must have a USCG approved life jacket and appropriate footwear",
      "All class participants must have on file a Rocky Fleet Usage Agreement for Class Participation",
      "All junior sailors are required to have a membership in the Long Island Junior Sailing Association at the cost of $75 for the first child, $100 for two children, and $125 for three or more children. These fees will be billed to your Rocky account. Questions? Email: jrsailing@rockypointclub.com",
    ],
  },
  adult: {
    heading: "Adult Sailing Program & Mandatory Forms",
    requirements: [
      "All sailors must have properly fitted life jacket and appropriate footwear.",
      "All class participants must have on file a Rocky Fleet Usage Agreement for Class Participation",
      "In order to use one of the Club’s Ideal 18s outside of class and on your own as the skipper, you must be a CERTIFIED SKIPPER and sign the FLEET USAGE AGREEMENT. This must be done EVERY YEAR so that we can keep the registry current.",
    ],
    closing:
      "For a list of Rocky Adult Sailing programs and Rocky Regattas, visit the Sailing Calendar. Questions? Email: sailing@rockypointclub.com",
  },
};

export const juniorSailing = {
  heading: "Junior Sailing Programs",
  intro:
    "The Rocky Point Sailing Program is available to members and non-members between the ages of 6 and 17. Whether you are just starting out with Little Puffs or an experienced racer, we have something for everyone! Summer 2026 will offer a six-week sailing program. Members must register by May 15th.",
  scheduleLine:
    "Junior Sailing Program - June 23rd to July 31st (Class times are subject to change based on registrations and aquatic scheduling)",
  levels: [
    {
      name: "Little Puffs (6 - 8 years old)",
      body:
        "This class is a great introduction for first-time sailors. Small groups will be exposed to sailing on an Ideal 18 with an instructor onboard each boat. Young sailors will learn safety and good boating habits on the water with supervised tiller time.",
      times: ["Tuesdays - Fridays, 10:30 am - 12:30 pm (no class on swim meet days)"],
    },
    {
      name: "Opti 1 (8 - 11 years old)",
      body:
        "Opti 1 is geared toward learning to sail a small boat on your own. Sailors will learn the basics of sailing, including how to rig and maneuver a boat independently. As confidence grows and basic sailing skills are attained, these sailors will be encouraged to participate in the Rocky regattas.",
      times: ["Mondays, 9:25 am - 12:10 pm", "Tuesdays - Fridays, 1:00 - 4:00 pm"],
    },
    {
      name: "Opti 2 Racing Team (10 - 15 years old)",
      body:
        "For those eager to get out on the water and have fun, Opti 2 students will learn more advanced sailing skills, including racing rules, strategy, and tactics. These sailors are strongly encouraged to participate in the Ice Cream Cup regattas at Rocky, as well as those at local clubs.",
      requirement: "Requirement: Master Opti 1 skills",
      times: ["Mondays, 9:05 am - 11:50 am", "Tuesdays - Fridays, 1:45 - 4:45 pm"],
    },
    {
      name: "Feva & Laser 4.7/Radial (12 - 17 years old)",
      body:
        "More experienced sailors will enjoy sailing fast moving double-handed Fevas and Lasers. Classes will focus on sailing drills, heel control, basic aerodynamics, sail shape controls and self-rescue techniques. These sailors are strongly encouraged to participate in local regattas.",
      requirement: "Requirements: Master Opti 2 skills and meet minimum weight guidance",
      times: ["Mondays, 9:05 am - 11:50 am", "Tuesdays - Fridays, 1:30 - 4:30 pm"],
    },
  ],
  firstDay: {
    heading: "Required for the first day of class",
    items: [
      "All sailors must have on file the Rocky Liability and Medical Release form",
      "USCG-approved life vest with attached whistle",
      "Closed-toe water shoes (no flip flops)",
      "Sun shirt",
      "Sunblock",
      "Hat",
      "Water bottle",
      "Sunglasses with leash (recommended but not required)",
    ],
  },
  sections: [
    {
      heading: "Program Fees",
      paragraphs: [
        "Member fees are billed directly to your account. Non-members can pay the club directly via check prior to the start of the sailing program.",
      ],
    },
    {
      heading: "Non-member sailors",
      paragraphs: [
        "Junior Sailing is available to non-members between the ages of 6 and 17 on a space-available basis and subject to non-member rates. Please email jrsailing@rockypointclub.com with the name, age and sailing class of interest.",
      ],
    },
    {
      heading: "JSALIS Membership",
      paragraphs: [
        "All junior sailors are required to have a membership in the Junior Sailing Association of the Long Island Sound (JSALIS) at the cost of $75 for the first child, $100 for two children, and $125 for three or more children. These fees will be billed to your Rocky account. For more information and to register visit: https://jsalis.org/parents/roster-registration.",
      ],
    },
    {
      heading: "Boats",
      paragraphs: [
        "Opti 1, Opti 2, Feva & Laser classes require the sailor to have their own boat or rent one. You may request to rent a Rocky Optimist or Feva during the registration process and oversubscribed boats will be allocated by lottery. Boat Locker in Bridgeport, CT is also a great resource for summer boat rentals and will deliver to the club. Please contact Boat Locker directly for the latest pricing.",
      ],
    },
    {
      heading: "Equipment Maintenance and Repair",
      paragraphs: [
        "All boats and sailing equipment must pass safety check-in with one of Rocky’s sailing instructors before they can be used in the program. Please see the calendar for scheduled times. Junior sailors are responsible for their own equipment during the sailing season. Sailors who have rented boats from Rocky’s fleet are responsible for the care of their boat to class expectations. They are also responsible for notifying the instructors of breakage or damage. Sailors and their parents are ultimately responsible for the equipment.",
      ],
    },
    {
      heading: "Swim Test",
      paragraphs: [
        "All new and returning sailors are required to complete a swim test before the start of the program. This involves swimming from the Rocky Point docks to the first set of buoys and back while wearing a USCG-approved life vest with an attached whistle. While treading water, the sailors will also take off their life jackets, tread water for an additional one minute and then put their life jackets back on while in the water. It is mandatory that your child pass the swim test before participation in the program. Please see the calendar for scheduled times.",
      ],
    },
    {
      heading: "Regatta Preparation",
      paragraphs: [
        "Junior sailors may participate in JSA sponsored regattas for which they qualify by age, experience, and area. Rocky Point Club is in JSA Area B. A regatta fee is required for each race that each sailor chooses to enter. The Sailing Program Director will determine which sailors are eligible for each regatta. JSA sponsored regattas are done on ClubSpot. Parents are responsible for setting up a profile for each sailor and registering for each regatta.",
        "Parents/guardians are responsible for transporting their children and their boats to any regattas that they attend. Instructors cannot drive junior sailors. At least one adult per participating boat must be present to facilitate preparation and registration prior to a regatta at the regatta venue and facilitate the proper derigging and breakdown of boats and equipment after a regatta at the regatta venue.",
        "Optimists and Lasers can be transported on top of cars. Fevas must be transported by trailer. Boat trailers are considered a part of the vehicle to which they are attached. Make sure that your automobile liability insurance covers the trailer. All sailors and parents, including those renting Rocky boats, are responsible for making sure the boats and rigs, if applicable, are properly secured onto the trailer or vehicle for transport. All other equipment must be transported by car to the regatta venue.",
        "At regattas, parents and friends are welcome to watch the race from a distance on the water. Spectators must be careful not to create wakes or windage and must stay well clear of the racecourse. The Racing Rules of Sailing prohibit outside assistance of any kind during a race, and regatta rules may require that non-racers stay well-clear between races as well.",
        "To access the full JSA of LIS calendar please go to the JSA website at www.jsalis.org and click on Calendar at the top of the home page. Please refer to the following Regatta Preparation Guide for an overview of responsibilities on regatta days.",
      ],
    },
    {
      heading: "Weather Policy",
      paragraphs: [
        "We will make every effort to hold junior sailing classes on all scheduled program days, but the weather is unpredictable. Prior to each class, the head sailing instructor will consult with our waterfront staff to determine if it is safe for our sailors to head out on the water. On days with too much/too little wind or threat of a storm, junior sailors will participate in dryland lessons and/or sailing-related arts & crafts or games. On very hot days please be sure to send enough water and a reusable water bottle to be refilled throughout the day. Please be sure to check the weather daily and send any clothing or gear items your child may need.",
      ],
    },
    {
      heading: "Private Lessons",
      paragraphs: [
        "Rocky offers private lesson opportunities at the cost of $80 per hour. Please contact the Sailing Program Director to schedule.",
      ],
    },
  ],
  questionsEmail: "jrsailing@rockypointclub.com",
};

export const entertainment = {
  heading: "Entertainment & Event Information",
  // The live Entertainment page is a calendar. No event copy is invented here;
  // it links to the club's existing events calendar.
  calendarUrl: "https://www.rockypointclub.com/events-calendar",
  calendarLabel: "View the Events Calendar",
};

export const admissions = {
  heading: "Admissions",
  homeCta:
    "Interested in joining Rocky Point Club? Learn more about the admissions process here.",
  categories: [
    {
      name: "Senior Membership",
      formTitle: "RPC Senior Membership Request Form",
      criteriaLabel: "CRITERIA:",
      criteria: [
        "Must be 65 years of age",
        "Must have been a member of the club for 20 years",
        "Joint membership requires each member to meet the above criteria.",
      ],
      note: "Click here for the most current Senior Waiting List.",
      noteHref: "/admissions#senior-waiting-list",
    },
    {
      name: "Non-Resident Membership",
      formTitle: "Change Membership to Non-Resident Status",
      statement:
        "To: The Members of the RPC Board of Governors\n\nI request permission from the Rocky Point Club Board of Governors to change my membership status to that of Non-Resident. I certify that our primary residence is the address stated below which is located 50 or more miles from Greenwich. I have read and understand the provisions of the Club’s by-laws pertaining to Non-Resident Membership (as set forth below), including the fact that such membership is on an annual basis and at the discretion of the Board of Governors, and agree to comply with such provisions.",
      bylawHeading: "Article II, Section d. Non-Resident",
      bylaw:
        "Non-Resident Membership shall be available to Active, Senior, or Inactive Members who transfer primary residence to a location fifty or more miles from Greenwich, provided that such Member retains his or her Club Debenture and Bonds, purchases any new Debenture and Bonds issued during said period of Membership, and pays the annual dues and assessments prescribed for such Membership as required by these By-Laws. A Non-Resident Member shall have the right to vote but no locker facility will be reserved. Moreover, such Member's use of the Club facilities shall be limited to a period not to exceed three weeks in any fiscal year. The number of Non-Resident Members shall not exceed twelve (12). Non-Resident Membership shall be on an annual basis and at the discretion of the Board of Governors. A Non-Resident Member wishing to renew such status, or to request reinstatement as an Active Member must notify the Board of Governors in writing prior to February 1st . To fill a vacancy caused by the resignation or other reduction in the number of Active Members such Non-Resident Member shall have priority over any other applicant except an Inactive Member.",
    },
    {
      name: "Change of Membership Status to Inactive",
      formTitle: "Change of Membership Status to Inactive",
      statement: "To: Members of the Board of Governors",
    },
    {
      name: "Change from Individual to Joint Membership",
      formTitle: "Change from Individual to Joint Membership",
      statement:
        "To: The Members of the RPC Board of Governors\n\nI request permission from the Rocky Point Club Board of Governors to change my membership status from Individual to Joint membership. We hereby certify that I understand the requirements for such membership status as set forth in the Rocky Point Club bylaws and will fulfill all conditions set out therein. We further state that we will comply with the regulations stated in the by-laws and with the provisions of the Neighborhood Agreement governing the new status.",
    },
    {
      name: "Change Membership Status to Active",
      formTitle: "Change Membership Status to Active",
      statement:
        "To: The Members of the RPC Board of Governors\n\nI request permission from the Rocky Point Club Board of Governors to change my membership status to Active. I hereby certify that I understand the requirements for such membership status as set forth in the Rocky Point Club bylaws and will fulfill all conditions set out therein. We further state that we will comply with the regulations stated in the by-laws and with the provisions of the Neighborhood Agreement governing the new status.",
    },
  ],
  seniorWaitingList: {
    heading: "Senior Waiting List",
    // The live page also publishes a roster of named families. That personal
    // data is intentionally NOT hard-coded into this repository — it is a
    // member record the Board Secretary maintains and belongs in the
    // stage-two members area, not a public source tree. The instructional
    // text below is reproduced verbatim.
    instructions:
      "To apply for senior membership, please fill out the form on our website: https://www.rockypointclub.com/senior-membership. Please contact the RPC Board Secretary at secretary@rockypointclub.com if you have any questions regarding Senior Membership.",
    rosterNote:
      "The current Senior Waiting List roster is maintained by the Board Secretary and will live in the members area (stage two).",
  },
};

export const membersArea = {
  heading: "Members Only",
  // Placeholder only. The live members-only section (Photo Directory, Club
  // Dues & Fees, Club Forms, Member Information, Rocky Merchandise, Rocky
  // Photo Album, Rocky Pointer, FSCL Club Information, Tennis, Video,
  // Contact Information) is password-protected and out of scope for stage
  // one. No member content is reproduced or invented here.
  note:
    "The members-only section is moving behind a secure login in stage two. For now, members continue to use the existing site.",
  sections: [
    "Photo Directory",
    "Club Dues & Fees",
    "Club Forms",
    "Member Information",
    "Rocky Merchandise",
    "Rocky Photo Album",
    "Rocky Pointer",
    "FSCL Club Information",
    "Tennis",
    "Video",
    "Contact Information",
  ],
};

export const contact = {
  heading: "Contact Us",
  directionsHeading: "Directions:",
  directionsIntro: "From Exit 5 on I-95 (Total Distance 2.6 miles):",
  directions: [
    "Turn right onto U.S. 1 N/E Putnam Ave",
    "Turn right onto Sound Beach Ave",
    "Turn right to stay on Sound Beach Ave",
    "Turn right onto Shore Rd",
    "Take the 2nd left onto Rocky Point Rd",
    "Rocky Point Club will be the end of the road",
  ],
  speedNotice:
    "NOTE THE SPEED LIMIT ON ROCKY POINT ROAD IS 15 MPH. PLEASE BE CONSIDERATE TO OUR NEIGHBORS",
  troubleshootingHeading: "Troubleshooting:",
  troubleshooting: [
    "If you have changes to your email address or are not receiving Rocky Point communication please contact us at info@rockypointclub.com",
    "Check your spam folder",
    "Drag Rocky Point emails back into your inbox",
    "Add Rocky Point emails to your contacts to ensure future emails do not get blocked or sent to spam folder.",
  ],
};
