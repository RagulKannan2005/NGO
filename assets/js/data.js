// assets/js/data.js

const programs = [
  {
    id: 1,
    title: "Conflict Resolution Fundamentals",
    level: "Beginner",
    duration: "2 Weeks",
    description:
      "Learn the core basics of identifying, addressing, and resolving workplace and community conflicts.",
    instructor: "Dr. Sarah Jenkins",
    modules: 4,
  },
  {
    id: 2,
    title: "Advanced Mediation for Leaders",
    level: "Advanced",
    duration: "4 Weeks",
    description:
      "Equip your leadership team with advanced techniques for high-stakes mediation and negotiation.",
    instructor: "Prof. Michael Aris",
    modules: 8,
  },
  {
    id: 3,
    title: "Youth & Gender Mediation",
    level: "Intermediate",
    duration: "3 Weeks",
    description:
      "Specialized training focused on resolving conflicts involving youth and marginalized gender groups.",
    instructor: "Elena Rodriguez",
    modules: 6,
  },
  {
    id: 4,
    title: "Crisis Communication Strategy",
    level: "Intermediate",
    duration: "2 Weeks",
    description:
      "Master the art of communicating effectively and de-escalating tension during organizational crises.",
    instructor: "David Chen",
    modules: 4,
  },
  {
    id: 5,
    title: "Community Peacebuilding",
    level: "Beginner",
    duration: "4 Weeks",
    description:
      "An introductory course to grassroots peacebuilding initiatives and community restoration.",
    instructor: "Dr. Ayesha Tariq",
    modules: 5,
  },
];

// High-level impact KPIs & stats
const impactStats = [
  {
    id: "ngos-trained",
    label: "NGOs trained",
    value: "520+",
    change: "+24% this year",
    description:
      "Organizations that enrolled at least one cohort in a conflict resolution pathway.",
  },
  {
    id: "learners",
    label: "Learners trained",
    value: "8,400+",
    change: "+1,200 in the last 6 months",
    description:
      "Front-line staff, volunteers, and coordinators who completed a full training track.",
  },
  {
    id: "completion",
    label: "Average completion rate",
    value: "92%",
    change: "Consistently above 85%",
    description:
      "Learners who reach the final module of at least one program they start.",
  },
  {
    id: "regions",
    label: "Countries & regions",
    value: "18",
    change: "Presence across 3 continents",
    description:
      "Active NGOs deploying graduates in Africa, South Asia, and Latin America.",
  },
  {
    id: "mediated-cases",
    label: "Cases mediated",
    value: "1,150+",
    change: "Self‑reported by partner NGOs",
    description:
      "Incidents where trained staff applied course tools to de‑escalate conflict.",
  },
  {
    id: "live-workshops",
    label: "Live workshops delivered",
    value: "230+",
    change: "Blended with self‑paced modules",
    description:
      "Facilitated sessions combining role‑plays, simulations, and local case work.",
  },
];

// Simple impact timeline for the Impact page
const impactTimeline = [
  { year: 2022, learners: 1200 },
  { year: 2023, learners: 2600 },
  { year: 2024, learners: 4100 },
  { year: 2025, learners: 6200 },
  { year: 2026, learners: 8400 },
];

// Case studies linked back to programs via programId
const impactStories = [
  {
    orgName: "Global Peace Initiative",
    country: "Kenya",
    programId: 1,
    headline: "Field teams standardize de‑escalation protocol in informal settlements",
    summary:
      "After completing Conflict Resolution Fundamentals, community mediators in Nairobi created a shared checklist for responding to neighborhood disputes.",
    quote:
      "We went from reacting case by case to having a common language and process for every incident.",
  },
  {
    orgName: "HelpNet",
    country: "Philippines",
    programId: 4,
    headline: "Crisis communication playbooks reduce rumor‑driven escalations",
    summary:
      "Program managers adapted templates from Crisis Communication Strategy into SMS and radio scripts for rapid updates during flooding.",
    quote:
      "Because our messages were clear and coordinated, rumors dropped and partners trusted our updates.",
  },
  {
    orgName: "Action Aid Collective",
    country: "Ghana",
    programId: 3,
    headline: "Youth mediators lead difficult conversations on gender and power",
    summary:
      "Graduates of Youth & Gender Mediation now co‑facilitate dialogues between traditional leaders and youth groups.",
    quote:
      "Young people who were previously silent now hold space for conversations elders once avoided.",
  },
  {
    orgName: "Borderlands Relief Network",
    country: "Colombia",
    programId: 2,
    headline: "Senior staff unlock stalled negotiations with local partners",
    summary:
      "Leadership teams used tools from Advanced Mediation for Leaders to re‑enter talks with a coalition of community groups.",
    quote:
      "We finally had a framework for separating people from problems and designing options together.",
  },
];

// Regional impact snapshot
const regionalImpact = [
  {
    region: "East Africa",
    ngos: 140,
    learners: 2600,
    highlight:
      "Strong uptake among organizations working in urban informal settlements and border districts.",
    focusAreas: ["Community mediation", "Youth leadership"],
  },
  {
    region: "South Asia",
    ngos: 190,
    learners: 3200,
    highlight:
      "Blended cohorts of local NGOs and international partners piloting shared incident protocols.",
    focusAreas: ["Crisis communication", "Staff wellbeing"],
  },
  {
    region: "Latin America",
    ngos: 110,
    learners: 1600,
    highlight:
      "Organizations integrating peacebuilding modules into broader protection and livelihoods programs.",
    focusAreas: ["Community mediation", "Gender‑responsive programming"],
  },
  {
    region: "Middle East & North Africa",
    ngos: 80,
    learners: 1000,
    highlight:
      "Remote learning tracks supporting teams that cannot gather in centralized hubs.",
    focusAreas: ["Early warning", "Partner coordination"],
  },
];
