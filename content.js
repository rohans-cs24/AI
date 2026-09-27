/*
=========================================================
MAZE SOLVING PRESENTATION CONTENT
=========================================================

This file contains EVERYTHING shown on the presentation
cards.

To change what your team sees/says:

1. Find the slide.
2. Change the "heading".
3. Change the "content".

Themes:

pink   → Part 1: Maze Problem
yellow → Part 2: Agent
blue   → Part 3: Task Environment
red    → Part 4: Maze Agent Logic
*/


const presentation = {

  slides: [

    // =====================================================
    // SLIDE 1
    // =====================================================

    {
      theme: "pink",
      section: "Introduction",
      heading: "Maze Solving",
      type: "title",

      content: `
        <p><strong>AI PPT</strong></p>

        <p>
          By:<br>
          Rohan S Mirjankar<br>
          Sannidhi Patil<br>
          Spoorthi T J<br>
          Sarveshwari Rao B
        </p>
      `
    },


    // =====================================================
    // SLIDE 2
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "What is the maze problem??",
      type: "question",

      content: `
        <p>
          First, we look at the basic maze problem and
          understand what the AI has to solve.
        </p>
      `
    },


    // =====================================================
    // SLIDE 3
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "Maze Solving",

      content: `
        <p>
          Maze solving is the process of finding a valid
          path from a given starting point to a destination
          in a maze while avoiding walls and obstacles.
        </p>

        <p>
          In AI, maze solving is a
          <strong>search problem</strong> where an agent
          explores different possible states and actions
          to find a path from the initial state to the
          goal state.
        </p>
      `
    },


    // =====================================================
    // SLIDE 4
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "Problem Statement",

      content: `
        <p>
          We have a maze containing:
        </p>

        <ul>
          <li>Start position (S)</li>
          <li>Goal position (G)</li>
          <li>Walls</li>
          <li>Open paths</li>
        </ul>

        <p>
          <strong>Objective:</strong>
          Find a valid path from the initial state to the
          goal state by searching through the possible
          states of the maze.
        </p>
      `
    },


    // =====================================================
    // SLIDE 5
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "Example Maze",

      content: `
        <p>
          This slide shows an example maze that the agent
          needs to solve.
        </p>

        <p>
          Focus on the <strong>start</strong>,
          <strong>goal</strong>, walls, and available paths.
        </p>
      `
    },


    // =====================================================
    // SLIDE 6
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "Example Maze",

      content: `
        <p>
          The maze is made up of cells that the agent can
          either move through or cannot enter.
        </p>

        <p>
          The walls restrict the possible routes available
          to the agent.
        </p>
      `
    },


    // =====================================================
    // SLIDE 7
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "Example Maze",

      content: `
        <p>
          The important distinction here is between
          <strong>blocked cells</strong> and
          <strong>open cells</strong>.
        </p>

        <p>
          The agent has to use this information while
          searching for the goal.
        </p>
      `
    },


    // =====================================================
    // SLIDE 8
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "Example Maze",

      content: `
        <p>
          <strong>WALL</strong> cells cannot be entered
          by the agent.
        </p>

        <p>
          Open cells form the possible routes through
          the maze.
        </p>
      `
    },


    // =====================================================
    // SLIDE 9
    // =====================================================

    {
      theme: "pink",
      section: "Part 1",
      heading: "State Representation",

      content: `
        <p>
          <strong>What is a State?</strong>
        </p>

        <p>
          A state represents the current position of the
          AI agent in the maze.
        </p>

        <p>
          We can represent the current state as
          <strong>(row, column)</strong>.
        </p>

        <p>
          For example,
          <strong>(1,1)</strong> means the agent is in
          row 1 and column 1.
        </p>
      `
    },


    // =====================================================
    // SLIDE 10
    // =====================================================

    {
      theme: "yellow",
      section: "Part 2",
      heading: "What is an Agent?? And how is it gonna solve mazes??",
      type: "question",

      content: `
        <p>
          Now we move from the maze itself to the
          <strong>AI agent</strong> that interacts with it.
        </p>
      `
    },


    // =====================================================
    // SLIDE 11
    // =====================================================

    {
      theme: "yellow",
      section: "Part 2",
      heading: "Agent",

      content: `
        <p>
          An agent is anything that can be viewed as
          perceiving its environment through
          <strong>sensors</strong> and acting upon that
          environment through <strong>effectors</strong>.
        </p>

        <p>
          Examples include humans and animals, robots and
          software agents, and temperature-control systems.
        </p>
      `
    },


    // =====================================================
    // SLIDE 12
    // =====================================================

    {
      theme: "yellow",
      section: "Part 2",
      heading: "Maze Agent",

      content: `
        <p>
          A <strong>Maze Agent</strong> is an intelligent
          agent that finds a path from a start position
          to a goal by perceiving the maze and selecting
          appropriate movements while avoiding walls.
        </p>
      `
    },


    // =====================================================
    // SLIDE 13
    // =====================================================

    {
      theme: "yellow",
      section: "Part 2",
      heading: "Maze Agent",

      content: `
        <p>
          The maze provides the environment and the agent
          interacts with it.
        </p>

        <p>
          The agent receives maze data, checks possible
          movements, and chooses what to do next.
        </p>
      `
    },


    // =====================================================
    // SLIDE 14
    // =====================================================

    {
      theme: "yellow",
      section: "Part 2",
      heading: "Maze Agent",

      content: `
        <p>
          The agent uses <strong>MAZE DATA</strong>
          to understand the environment.
        </p>

        <p>
          Based on this data, it determines the possible
          <strong>MOVES</strong> it can perform.
        </p>

        <p>
          The basic cycle is:
          <strong>observe → decide → move</strong>.
        </p>
      `
    },


    // =====================================================
    // SLIDE 15
    // =====================================================

    {
      theme: "yellow",
      section: "Part 2",
      heading: "Actions",

      content: `
        <p>
          There are 4 actions that can be attempted:
        </p>

        <ul>
          <li>⬆️ Move Up</li>
          <li>⬇️ Move Down</li>
          <li>⬅️ Move Left</li>
          <li>➡️ Move Right</li>
          <li>Or simply, <strong>Stop moving</strong></li>
        </ul>
      `
    },


    // =====================================================
    // SLIDE 16
    // =====================================================

    {
      theme: "blue",
      section: "Part 3",
      heading: "What is a Task Environment?? Why is it important??",
      type: "question",

      content: `
        <p>
          Next, we define the
          <strong>task environment</strong>
          in which our maze agent operates.
        </p>
      `
    },


    // =====================================================
    // SLIDE 17
    // =====================================================

    {
      theme: "blue",
      section: "Part 3",
      heading: "Task Environment",

      content: `
        <p>
          A task environment is the world or situation
          in which an intelligent agent operates.
        </p>

        <p>
          In our case, it's a maze containing a starting
          point, destination, paths, and obstacles, where
          the agent must find a path to reach the goal.
        </p>

        <p>
          It describes:
        </p>

        <ul>
          <li>What the agent needs to achieve</li>
          <li>What the agent can observe</li>
          <li>What actions the agent can perform</li>
          <li>What kind of conditions the agent works under</li>
        </ul>
      `
    },


    // =====================================================
    // SLIDE 18
    // =====================================================

    {
      theme: "blue",
      section: "Part 3",
      heading: "Nature Of Environment",

      content: `
        <ul>
          <li>
            <strong>Agent:</strong>
            Maze Agent
          </li>

          <li>
            <strong>Performance Measure:</strong>
            Reach the goal using the shortest path
          </li>

          <li>
            <strong>Environment:</strong>
            Maze with walls, paths, start and goal;
            static, discrete, fully observable
          </li>

          <li>
            <strong>Actuators:</strong>
            Move Up, Down, Left, Right
          </li>

          <li>
            <strong>Sensors:</strong>
            Detect current position, walls, and goal
          </li>
        </ul>
      `
    },


    // =====================================================
    // SLIDE 19
    // =====================================================

    {
      theme: "blue",
      section: "Part 3",
      heading: "Properties of Task Environment",

      content: `
        <ul>

          <li>
            <strong>Fully Observable:</strong>
            The agent can see the maze, including walls,
            paths, start and goal.
          </li>

          <li>
            <strong>Single-Agent:</strong>
            Only one AI agent is solving the maze.
          </li>

          <li>
            <strong>Deterministic:</strong>
            If the agent chooses "Move Right",
            it moves right.
          </li>

          <li>
            <strong>Sequential:</strong>
            Each movement affects the agent's next position.
          </li>

          <li>
            <strong>Static:</strong>
            The maze doesn't change while the agent
            is solving it.
          </li>

          <li>
            <strong>Discrete:</strong>
            The agent moves between distinct cells.
          </li>

          <li>
            <strong>Known:</strong>
            The agent knows the maze layout,
            possible movements, and rules beforehand.
          </li>

        </ul>
      `
    },


    // =====================================================
    // SLIDE 20
    // =====================================================

    {
      theme: "red",
      section: "Part 4",
      heading: "What is the logic behind Maze agent ??",
      type: "question",

      content: `
        <p>
          Finally, we look at the actual search logic
          used by the maze agent to find the path.
        </p>

        <p>
          Our agent uses
          <strong>Breadth-First Search (BFS)</strong>
          to explore the maze.
        </p>
      `
    },


    // =====================================================
    // SLIDE 21
    // =====================================================

    {
      theme: "red",
      section: "Part 4",
      heading: "Agent Program",

      content: `
        <p>
          The agent program uses
          <strong>Breadth-First Search (BFS)</strong>
          to explore the maze.
        </p>

        <div class="code">

Function MAZE-AGENT(location, goal, blocked)
returns an action

If location = goal
    return STOP

Initialize QUEUE with location
Mark location as VISITED
Set PARENT(location) = NULL

while QUEUE is not empty:

    current ← DEQUEUE(QUEUE)

    If current = goal:
        break

    For each direction in
    {RIGHT, DOWN, LEFT, UP}:

        next ← adjacent cell in that direction

        If next is not blocked
        AND next is not VISITED:

            Mark next as VISITED

            PARENT(next) ← current

            ENQUEUE(QUEUE, next)

If goal was not reached:
    return NO-PATH

Trace the parent relationships
to reconstruct the path

        </div>
      `
    },


    // =====================================================
    // SLIDE 22
    // =====================================================

    {
      theme: "red",
      section: "Part 4",
      heading: "Simulation",

      content: `
        <p>
          Now we can see the actual
          <strong>simulation</strong>
          of our maze-solving agent.
        </p>

        <p>
          The agent starts from the initial position
          and explores the maze according to the BFS logic.
        </p>

        <p>
          Once the goal is found, the final path can be
          reconstructed and the agent can follow that path
          to reach the destination.
        </p>
      `
    },


    // =====================================================
    // SLIDE 23
    // =====================================================

    {
      theme: "red",
      section: "Conclusion",
      heading: "THANK YOU",

      content: `
        <p>
          That's how we model and solve a maze as an
          AI search problem.
        </p>

        <p>
          We looked at the agent, its states and actions,
          the task environment, and how BFS allows the
          agent to find a path.
        </p>

        <p>
          <strong>Questions?</strong>
        </p>
      `
    }

  ]

};
